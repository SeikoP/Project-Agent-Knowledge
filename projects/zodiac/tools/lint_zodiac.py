#!/usr/bin/env python3
"""Lint Writer JSON against measurable Zodiac v9 voice rules.

Stdlib only. Expected Writer payload:
{"ideas": [{"slides": [{"content_blocks": [{"type": "body", "text": "..."}]}]}]}
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path
from typing import Iterable

PROSE_BLOCK_TYPES = {"body", "callout"}
LEADING_PRONOUNS = {
    "bạn", "họ", "mình", "tôi", "cậu", "nó", "anh", "em", "người",
}
WORD_RE = re.compile(r"\w+", re.UNICODE)
SENTENCE_RE = re.compile(r"[^.!?…]+[.!?…]*", re.UNICODE)
BANNED_CONNECTOR_RE = re.compile(
    r"\b(nhưng|trong\s+khi|trong\s+lúc)\b",
    re.IGNORECASE | re.UNICODE,
)
PAIRED_PATTERNS = {
    "khong_chi_ma_con": re.compile(
        r"không\s+chỉ\b.*?\bmà\s+còn\b",
        re.IGNORECASE | re.UNICODE,
    ),
    "khong_phai_ma_la": re.compile(
        r"không\s+phải\b.*?\bmà\s+là\b",
        re.IGNORECASE | re.UNICODE,
    ),
}
GENERALIZATION_START_RE = re.compile(
    r"^\s*(tóm\s+lại|vì\s+vậy|điều\s+này)\b",
    re.IGNORECASE | re.UNICODE,
)
MAX_WORDS_PER_SENTENCE = 18
MAX_PAIRED_CONSTRUCTION_PER_POST = 1


def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFC", str(text or "")).strip()


def load_blacklist(path: Path) -> list[str]:
    terms: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = normalize_text(raw)
        if not value or value.startswith("#"):
            continue
        terms.append(value)
    return terms


def _blacklist_patterns(blacklist: Iterable[str]) -> list[tuple[str, re.Pattern[str]]]:
    return [
        (
            term,
            re.compile(
                rf"(?<!\w){re.escape(normalize_text(term))}(?!\w)",
                re.IGNORECASE | re.UNICODE,
            ),
        )
        for term in blacklist
        if normalize_text(term)
    ]


def sentences(text: str) -> list[str]:
    value = normalize_text(text)
    return [
        match.group(0).strip()
        for match in SENTENCE_RE.finditer(value)
        if match.group(0).strip()
    ]


def word_count(text: str) -> int:
    return len(WORD_RE.findall(normalize_text(text)))


def opening_signature(text: str) -> str:
    words = [word.casefold() for word in WORD_RE.findall(normalize_text(text))]
    if words and words[0] in LEADING_PRONOUNS:
        words = words[1:]
    if len(words) < 2:
        return ""
    return " ".join(words[:2])


def prose_block_texts(slide: dict) -> list[str]:
    blocks = slide.get("content_blocks")
    if not isinstance(blocks, list):
        return []
    return [
        normalize_text(block.get("text") or "")
        for block in blocks
        if (
            isinstance(block, dict)
            and block.get("type") in PROSE_BLOCK_TYPES
            and normalize_text(block.get("text") or "")
        )
    ]


def slide_text(slide: dict) -> str:
    return " ".join(prose_block_texts(slide)).strip()


def _error(slide: int, sentence: str, rule: str) -> dict:
    return {"slide": slide, "câu": sentence, "rule": rule}


def validate_payload_schema(payload: object) -> list[dict]:
    errors: list[dict] = []
    if not isinstance(payload, dict):
        return [_error(0, "", "schema.top_level_must_be_object")]
    if "ideas" not in payload:
        return [_error(0, "", "schema.ideas_required")]
    if set(payload) != {"ideas"}:
        errors.append(_error(0, "", "schema.top_level_must_only_contain_ideas"))
    ideas = payload.get("ideas")
    if not isinstance(ideas, list):
        errors.append(_error(0, "", "schema.ideas_must_be_list"))
        return errors
    for idea in ideas:
        if not isinstance(idea, dict):
            errors.append(_error(0, "", "schema.idea_must_be_object"))
        elif not isinstance(idea.get("slides"), list):
            errors.append(_error(0, "", "schema.slides_required"))
    return errors


def lint_idea(idea: dict, blacklist: Iterable[str]) -> list[dict]:
    errors: list[dict] = []
    slides = idea.get("slides")
    if not isinstance(slides, list):
        return errors

    blacklist_patterns = _blacklist_patterns(blacklist)
    paired_occurrences: dict[str, list[tuple[int, str, str]]] = {
        name: [] for name in PAIRED_PATTERNS
    }
    previous_opening = ""

    for slide_index, slide in enumerate(slides, 1):
        if not isinstance(slide, dict):
            continue
        block_texts = prose_block_texts(slide)
        text = " ".join(block_texts).strip()

        opening = opening_signature(text)
        if opening and previous_opening and opening == previous_opening:
            errors.append(_error(
                slide_index,
                text,
                "voice.adjacent_slides_same_opening_signature",
            ))
        if opening:
            previous_opening = opening

        sentence_records: list[str] = []
        for block_text in block_texts:
            for sentence in sentences(block_text):
                sentence_records.append(sentence)
                if word_count(sentence) > MAX_WORDS_PER_SENTENCE:
                    errors.append(_error(
                        slide_index,
                        sentence,
                        f"voice.sentence_over_{MAX_WORDS_PER_SENTENCE}_words",
                    ))
                if BANNED_CONNECTOR_RE.search(sentence):
                    errors.append(_error(
                        slide_index,
                        sentence,
                        "voice.banned_clause_connector",
                    ))

                for term, pattern in blacklist_patterns:
                    if pattern.search(sentence):
                        errors.append(_error(
                            slide_index,
                            sentence,
                            f"voice.blacklist:{term}",
                        ))

                for name, pattern in PAIRED_PATTERNS.items():
                    for match in pattern.finditer(sentence):
                        paired_occurrences[name].append(
                            (slide_index, sentence, match.group(0))
                        )

        if sentence_records and GENERALIZATION_START_RE.search(sentence_records[-1]):
            errors.append(_error(
                slide_index,
                sentence_records[-1],
                "voice.generalizing_ending",
            ))

    for name, occurrences in paired_occurrences.items():
        for slide_index, sentence, _match in occurrences[MAX_PAIRED_CONSTRUCTION_PER_POST:]:
            errors.append(_error(
                slide_index,
                sentence,
                f"voice.{name}_over_{MAX_PAIRED_CONSTRUCTION_PER_POST}_per_post",
            ))

    return errors


def lint_payload(payload: object, blacklist: Iterable[str]) -> list[dict]:
    """Run voice lint only; schema validation is intentionally separate."""
    if not isinstance(payload, dict):
        return []
    ideas = payload.get("ideas")
    if not isinstance(ideas, list):
        return []
    errors: list[dict] = []
    for idea in ideas:
        if isinstance(idea, dict):
            errors.extend(lint_idea(idea, blacklist))
    return errors


def lint_document(payload: object, blacklist: Iterable[str]) -> list[dict]:
    return [
        *validate_payload_schema(payload),
        *lint_payload(payload, blacklist),
    ]


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
        print(json.dumps(
            [_error(0, "", f"io_or_json:{exc}")],
            ensure_ascii=False,
            indent=2,
        ))
        return 2

    errors = lint_document(payload, blacklist)
    print(json.dumps(errors, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
