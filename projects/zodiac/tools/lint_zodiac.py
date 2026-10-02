#!/usr/bin/env python3
"""Lint Writer JSON against measurable Zodiac v9.7 prose rules.

Stdlib only. Extra top-level payload keys are ignored by voice lint.
Only configured prose block types are linted; the default follows the current
carousel contract and includes body plus callout blocks.

v9.7 intentionally keeps lint narrow: schema, hard blacklist terms and
generalizing endings. Rhythm, connectors, filler, opening variety and sentence
length are reviewed by the editorial/style pass instead of hard keyword quotas.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Iterable


SENTENCE_RE = re.compile(r"[^.!?…]+[.!?…]*", re.UNICODE)
GENERALIZATION_START_RE = re.compile(
    r"^\s*(tóm\s+lại|vì\s+vậy|điều\s+này\s+cho\s+thấy)\b",
    re.IGNORECASE | re.UNICODE,
)
DEFAULT_PROSE_BLOCK_TYPES = frozenset({"body", "callout"})
GENERALIZATION_BLACKLIST_TERMS = frozenset(
    {"tóm lại", "vì vậy", "điều này cho thấy"}
)


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
    normalized_blacklist = [normalize_text(term) for term in blacklist]
    blacklist_patterns = [(term, term_regex(term)) for term in normalized_blacklist]

    for slide_index, slide in enumerate(idea["slides"], 1):
        block_texts = (
            slide_block_texts(slide, prose_block_types)
            if isinstance(slide, dict)
            else []
        )

        for block_text in block_texts:
            block_sentences = sentences(block_text)
            for sentence_index, sentence in enumerate(block_sentences, 1):
                generalization_match = None
                if sentence_index == len(block_sentences):
                    generalization_match = GENERALIZATION_START_RE.search(sentence)
                    if generalization_match:
                        errors.append(
                            _error(slide_index, sentence, "voice.generalizing_ending")
                        )

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
