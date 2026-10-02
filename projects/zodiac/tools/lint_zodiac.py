#!/usr/bin/env python3
"""Lint Writer JSON against measurable Zodiac v9 voice rules.

Stdlib only. Expected payload:
{"ideas": [{"slides": [{"content_blocks": [{"text": "..."}]}]}]}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

WORD_RE = re.compile(r"[\wÀ-ỹĐđ]+", re.UNICODE)
SENTENCE_RE = re.compile(r"[^.!?…]+[.!?…]*", re.UNICODE)
BANNED_CONNECTOR_RE = re.compile(r"\b(nhưng|trong\s+khi|trong\s+lúc)\b", re.IGNORECASE | re.UNICODE)
PAIRED_PATTERNS = {
    "khong_chi_ma_con": re.compile(r"không\s+chỉ\b.*?\bmà\s+còn\b", re.IGNORECASE | re.UNICODE),
    "khong_phai_ma_la": re.compile(r"không\s+phải\b.*?\bmà\s+là\b", re.IGNORECASE | re.UNICODE),
}
GENERALIZATION_START_RE = re.compile(
    r"^\s*(tóm\s+lại|vì\s+vậy|điều\s+này)\b",
    re.IGNORECASE | re.UNICODE,
)
MAX_WORDS_PER_SENTENCE = 18  # TODO-TUNE
MAX_PAIRED_CONSTRUCTION_PER_POST = 1


def load_blacklist(path: Path) -> list[str]:
    terms: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = raw.strip()
        if not value or value.startswith("#"):
            continue
        terms.append(value)
    return terms


def sentences(text: str) -> list[str]:
    return [
        match.group(0).strip()
        for match in SENTENCE_RE.finditer(text or "")
        if match.group(0).strip()
    ]


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text or ""))


def first_word(text: str) -> str:
    match = WORD_RE.search(text or "")
    return match.group(0).casefold() if match else ""


def slide_block_texts(slide: dict) -> list[str]:
    blocks = slide.get("content_blocks")
    if not isinstance(blocks, list):
        return []
    return [
        str(block.get("text") or "").strip()
        for block in blocks
        if isinstance(block, dict) and str(block.get("text") or "").strip()
    ]


def slide_text(slide: dict) -> str:
    return " ".join(slide_block_texts(slide)).strip()


def _error(slide: int, sentence: str, rule: str) -> dict:
    return {"slide": slide, "câu": sentence, "rule": rule}


def lint_idea(idea: dict, blacklist: Iterable[str]) -> list[dict]:
    errors: list[dict] = []
    slides = idea.get("slides")
    if not isinstance(slides, list):
        return [_error(0, "", "schema.slides_required")]

    all_slide_texts = [slide_text(slide) if isinstance(slide, dict) else "" for slide in slides]
    all_block_texts: list[str] = []

    previous_opening = ""
    for slide_index, slide in enumerate(slides, 1):
        block_texts = slide_block_texts(slide) if isinstance(slide, dict) else []
        text = " ".join(block_texts).strip()
        opening = first_word(text)
        if opening and previous_opening and opening == previous_opening:
            errors.append(_error(slide_index, text, "voice.adjacent_slides_same_opening"))
        if opening:
            previous_opening = opening

        for block_text in block_texts:
            all_block_texts.append(block_text)
            block_sentences = sentences(block_text)
            for sentence_index, sentence in enumerate(block_sentences, 1):
                if word_count(sentence) > MAX_WORDS_PER_SENTENCE:
                    errors.append(_error(
                        slide_index,
                        sentence,
                        f"voice.sentence_over_{MAX_WORDS_PER_SENTENCE}_words",
                    ))
                if BANNED_CONNECTOR_RE.search(sentence):
                    errors.append(_error(slide_index, sentence, "voice.banned_clause_connector"))
                if sentence_index == len(block_sentences) and GENERALIZATION_START_RE.search(sentence):
                    errors.append(_error(slide_index, sentence, "voice.generalizing_ending"))

                lowered = sentence.casefold()
                for term in blacklist:
                    if term.casefold() in lowered:
                        errors.append(_error(slide_index, sentence, f"voice.blacklist:{term}"))

    post_text = ". ".join(all_block_texts)
    for name, pattern in PAIRED_PATTERNS.items():
        matches = list(pattern.finditer(post_text))
        if len(matches) > MAX_PAIRED_CONSTRUCTION_PER_POST:
            errors.append(_error(
                0,
                matches[MAX_PAIRED_CONSTRUCTION_PER_POST].group(0),
                f"voice.{name}_over_{MAX_PAIRED_CONSTRUCTION_PER_POST}_per_post",
            ))

    return errors


def lint_payload(payload: dict, blacklist: Iterable[str]) -> list[dict]:
    if not isinstance(payload, dict) or set(payload) != {"ideas"}:
        return [_error(0, "", "schema.top_level_must_only_contain_ideas")]
    ideas = payload.get("ideas")
    if not isinstance(ideas, list):
        return [_error(0, "", "schema.ideas_must_be_list")]

    errors: list[dict] = []
    for idea_index, idea in enumerate(ideas, 1):
        if not isinstance(idea, dict):
            errors.append(_error(0, "", f"schema.idea_{idea_index}_must_be_object"))
            continue
        errors.extend(lint_idea(idea, blacklist))
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
        print(json.dumps([{"slide": 0, "câu": "", "rule": f"io_or_json:{exc}"}], ensure_ascii=False, indent=2))
        return 2

    errors = lint_payload(payload, blacklist)
    print(json.dumps(errors, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
