#!/usr/bin/env python3
"""Lint Writer JSON against measurable Zodiac v9.3 voice rules.

Stdlib only. Extra top-level payload keys are ignored by voice lint.
Only configured prose block types are linted; the default follows the current
carousel contract and includes body plus callout blocks.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Iterable


WORD_RE = re.compile(r"[\wÀ-ỹĐđ]+", re.UNICODE)
SENTENCE_RE = re.compile(r"[^.!?…]+[.!?…]*", re.UNICODE)
BANNED_CONNECTOR_RE = re.compile(
    r"(?<!\w)(trong\s+khi|trong\s+lúc)(?!\w)",
    re.IGNORECASE | re.UNICODE,
)
PAIRED_PATTERNS = {
    "khong_chi_ma_con": re.compile(
        r"(?<!\w)không\s+chỉ(?!\w).*?(?<!\w)mà\s+còn(?!\w)",
        re.IGNORECASE | re.UNICODE,
    ),
    "khong_phai_ma_la": re.compile(
        r"(?<!\w)không\s+phải(?!\w).*?(?<!\w)mà\s+là(?!\w)",
        re.IGNORECASE | re.UNICODE,
    ),
}
GENERALIZATION_START_RE = re.compile(
    r"^\s*(tóm\s+lại|vì\s+vậy|điều\s+này\s+cho\s+thấy)\b",
    re.IGNORECASE | re.UNICODE,
)
HEDGE_OPENER_RE = re.compile(r"^\s*kiểu\b", re.IGNORECASE | re.UNICODE)
FILLER_END_RE = re.compile(
    r"(?<!\w)(á|nha|luôn|liền|ghê|hà)(?!\w)(?=\s*(?:[,;:.!?…]|$))",
    re.IGNORECASE | re.UNICODE,
)

MAX_SYLLABLES_PER_SENTENCE = 24  # v9.2: allow fuller spoken sentences; 8–18 remains the preferred prose range.
MAX_PAIRED_CONSTRUCTION_PER_POST = 1
MAX_FILLERS_PER_SLIDE = 1
MAX_FILLERS_PER_POST = 3  # TODO-TUNE: validate against real Writer output before tightening.
DEFAULT_PROSE_BLOCK_TYPES = frozenset({"body", "callout"})
OPENING_PRONOUNS = frozenset({"bạn", "họ", "mình"})
GENERALIZATION_BLACKLIST_TERMS = frozenset({"tóm lại", "vì vậy", "điều này cho thấy"})


def normalize_text(text: object) -> str:
    return unicodedata.normalize("NFC", str(text or ""))


def load_blacklist(path: Path) -> list[str]:
    terms: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = normalize_text(raw).strip()
        if not value or value.startswith("#"):
            continue
        terms.append(value)
    return terms


def term_regex(term: str) -> re.Pattern[str]:
    normalized = normalize_text(term).casefold()
    return re.compile(
        r"(?<!\w)" + re.escape(normalized) + r"(?!\w)",
        re.IGNORECASE | re.UNICODE,
    )


def sentences(text: str) -> list[str]:
    out: list[str] = []
    for line in normalize_text(text).splitlines():
        out.extend(
            match.group(0).strip()
            for match in SENTENCE_RE.finditer(line)
            if match.group(0).strip()
        )
    return out


def syllable_count(text: str) -> int:
    """Approximate Vietnamese tiếng/âm tiết by whitespace-separated word tokens."""
    return len(WORD_RE.findall(normalize_text(text)))


def opening_signature(text: str) -> tuple[str, ...]:
    words = [token.casefold() for token in WORD_RE.findall(normalize_text(text))]
    if words[:2] == ["người", "ta"]:
        words = words[2:]
    elif words and words[0] in OPENING_PRONOUNS:
        words = words[1:]
    return tuple(words[:2])


def filler_terms(text: str) -> list[str]:
    normalized = normalize_text(text)
    return [match.group(1).casefold() for match in FILLER_END_RE.finditer(normalized)]


def slide_block_texts(
    slide: dict,
    prose_block_types: Iterable[str] = DEFAULT_PROSE_BLOCK_TYPES,
) -> list[str]:
    blocks = slide.get("content_blocks")
    if not isinstance(blocks, list):
        return []
    allowed = frozenset(prose_block_types)
    return [
        normalize_text(block.get("text")).strip()
        for block in blocks
        if (
            isinstance(block, dict)
            and block.get("type") in allowed
            and normalize_text(block.get("text")).strip()
        )
    ]


def slide_text(
    slide: dict,
    prose_block_types: Iterable[str] = DEFAULT_PROSE_BLOCK_TYPES,
) -> str:
    return " ".join(slide_block_texts(slide, prose_block_types)).strip()


def _error(slide: int, sentence: str, rule: str) -> dict:
    return {"slide": slide, "sentence": normalize_text(sentence), "rule": rule}


def validate_payload_schema(payload: object) -> list[dict]:
    if not isinstance(payload, dict) or "ideas" not in payload:
        return [_error(0, "", "schema.ideas_required")]
    ideas = payload.get("ideas")
    if not isinstance(ideas, list):
        return [_error(0, "", "schema.ideas_must_be_list")]

    errors: list[dict] = []
    for idea_index, idea in enumerate(ideas, 1):
        if not isinstance(idea, dict):
            errors.append(_error(0, "", f"schema.idea_{idea_index}_must_be_object"))
            continue
        if not isinstance(idea.get("slides"), list):
            errors.append(_error(0, "", f"schema.idea_{idea_index}_slides_required"))
    return errors


def lint_idea(
    idea: dict,
    blacklist: Iterable[str],
    prose_block_types: Iterable[str] = DEFAULT_PROSE_BLOCK_TYPES,
) -> list[dict]:
    errors: list[dict] = []
    slides = idea["slides"]

    normalized_blacklist = [normalize_text(term) for term in blacklist]
    blacklist_patterns = [(term, term_regex(term)) for term in normalized_blacklist]
    paired_counts = {name: 0 for name in PAIRED_PATTERNS}

    previous_opening: tuple[str, ...] = ()
    previous_fillers: set[str] = set()
    total_fillers = 0

    for slide_index, slide in enumerate(slides, 1):
        block_texts = (
            slide_block_texts(slide, prose_block_types)
            if isinstance(slide, dict)
            else []
        )
        text = " ".join(block_texts).strip()

        opening = opening_signature(text)
        if opening and previous_opening and opening == previous_opening:
            errors.append(_error(slide_index, text, "voice.adjacent_slides_same_opening"))
        previous_opening = opening

        current_fillers = filler_terms(text)
        total_fillers += len(current_fillers)
        if len(current_fillers) > MAX_FILLERS_PER_SLIDE:
            errors.append(
                _error(
                    slide_index,
                    text,
                    f"voice.filler_over_{MAX_FILLERS_PER_SLIDE}_per_slide",
                )
            )
        repeated = sorted(set(current_fillers) & previous_fillers)
        for filler in repeated:
            errors.append(
                _error(slide_index, text, f"voice.filler_repeated_adjacent:{filler}")
            )
        previous_fillers = set(current_fillers)

        for block_text in block_texts:
            block_sentences = sentences(block_text)
            for sentence_index, sentence in enumerate(block_sentences, 1):
                if syllable_count(sentence) > MAX_SYLLABLES_PER_SENTENCE:
                    errors.append(
                        _error(
                            slide_index,
                            sentence,
                            f"voice.sentence_over_{MAX_SYLLABLES_PER_SENTENCE}_syllables",
                        )
                    )
                if BANNED_CONNECTOR_RE.search(sentence):
                    errors.append(
                        _error(slide_index, sentence, "voice.banned_clause_connector")
                    )

                generalization_match = None
                if sentence_index == len(block_sentences):
                    generalization_match = GENERALIZATION_START_RE.search(sentence)
                    if generalization_match:
                        errors.append(
                            _error(slide_index, sentence, "voice.generalizing_ending")
                        )

                if HEDGE_OPENER_RE.search(sentence):
                    errors.append(_error(slide_index, sentence, "voice.hedge_opener"))

                lowered = normalize_text(sentence).casefold()
                generalization_term = (
                    " ".join(generalization_match.group(1).casefold().split())
                    if generalization_match
                    else ""
                )
                for term, pattern in blacklist_patterns:
                    normalized_term = " ".join(term.casefold().split())
                    if (
                        generalization_term
                        and normalized_term in GENERALIZATION_BLACKLIST_TERMS
                        and normalized_term == generalization_term
                    ):
                        continue
                    if pattern.search(lowered):
                        errors.append(
                            _error(slide_index, sentence, f"voice.blacklist:{term}")
                        )

                for name, pattern in PAIRED_PATTERNS.items():
                    for match in pattern.finditer(sentence):
                        paired_counts[name] += 1
                        if paired_counts[name] > MAX_PAIRED_CONSTRUCTION_PER_POST:
                            errors.append(
                                _error(
                                    slide_index,
                                    match.group(0),
                                    f"voice.{name}_over_{MAX_PAIRED_CONSTRUCTION_PER_POST}_per_post",
                                )
                            )

    if total_fillers > MAX_FILLERS_PER_POST:
        errors.append(
            _error(
                0,
                "",
                f"voice.filler_over_{MAX_FILLERS_PER_POST}_per_post",
            )
        )

    return errors


def lint_payload(
    payload: object,
    blacklist: Iterable[str],
    prose_block_types: Iterable[str] = DEFAULT_PROSE_BLOCK_TYPES,
) -> list[dict]:
    schema_errors = validate_payload_schema(payload)
    if schema_errors:
        return schema_errors

    errors: list[dict] = []
    for idea in payload["ideas"]:
        errors.extend(lint_idea(idea, blacklist, prose_block_types))
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument(
        "--blacklist",
        type=Path,
        default=Path(__file__).with_name("blacklist.txt"),
    )
    args = parser.parse_args(argv)

    try:
        payload = json.loads(args.json_file.read_text(encoding="utf-8"))
        blacklist = load_blacklist(args.blacklist)
    except (OSError, json.JSONDecodeError) as exc:
        print(
            json.dumps(
                [{"slide": 0, "sentence": "", "rule": f"io_or_json:{exc}"}],
                ensure_ascii=False,
                indent=2,
            )
        )
        return 2

    errors = lint_payload(payload, blacklist)
    print(json.dumps(errors, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
