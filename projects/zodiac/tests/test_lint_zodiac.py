from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINT_PATH = ROOT / "tools" / "lint_zodiac.py"
BLACKLIST_PATH = ROOT / "tools" / "blacklist.txt"
RULE_PATH = ROOT / "rules" / "content-design.md"

spec = importlib.util.spec_from_file_location("lint_zodiac", LINT_PATH)
lint_zodiac = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(lint_zodiac)

BLACKLIST = lint_zodiac.load_blacklist(BLACKLIST_PATH)


def payload(*slides: str) -> dict:
    return {
        "ideas": [{
            "idea_id": 1,
            "slides": [{
                "content_blocks": [
                    {"block_id": "body-1", "type": "body", "text": text}
                ]
            } for text in slides],
        }]
    }


class ZodiacVoiceLintTests(unittest.TestCase):
    def rules(self, *slides: str) -> list[str]:
        return [
            item["rule"]
            for item in lint_zodiac.lint_payload(payload(*slides), BLACKLIST)
        ]

    def test_good_calibration_examples_pass(self):
        good = (
            "Nhớ chuyện bạn kể hôm trước. Lần sau gặp còn hỏi: giờ ổn chưa?",
            "Thấy một điểm hay là khen đúng điểm đó.",
            "Nói chuyện chậm rãi. Điều gì nghĩ thật thì nói thật.",
        )
        for text in good:
            with self.subTest(text=text):
                self.assertEqual(self.rules(text), [])

    def test_sentence_limit_connector_and_blacklist_are_caught(self):
        rules = self.rules(
            "Xử Nữ nói chuyện chân thành nhưng vẫn tiếp cận từ tốn.",
            "Câu này dùng sự chú ý như một danh từ rất chung để giải thích hành vi đang xảy ra.",
            "Đây là một câu quá dài để kiểm tra giới hạn mười tám token trong linter tiếng Việt hiện tại của dự án.",
        )
        self.assertIn("voice.banned_clause_connector", rules)
        self.assertTrue(any(rule.startswith("voice.blacklist:") for rule in rules))
        self.assertIn("voice.sentence_over_18_words", rules)

    def test_nfc_normalization_and_blacklist_boundaries(self):
        nfd = unicodedata.normalize("NFD", "Sự chú ý đang nằm ở đây.")
        self.assertTrue(any(
            rule.startswith("voice.blacklist:")
            for rule in self.rules(nfd)
        ))
        self.assertFalse(any(
            rule == "voice.blacklist:qua đó"
            for rule in self.rules("Mình đi qua đó rồi về.")
        ))

    def test_opening_signature_uses_prose_and_ignores_leading_pronoun(self):
        p = {
            "ideas": [{
                "slides": [
                    {"content_blocks": [
                        {"type": "headline", "text": "Cùng một headline"},
                        {"type": "body", "text": "Bạn kể chuyện buồn."},
                    ]},
                    {"content_blocks": [
                        {"type": "headline", "text": "Cùng một headline"},
                        {"type": "body", "text": "Họ hỏi lại ngay."},
                    ]},
                ]
            }]
        }
        rules = [
            item["rule"]
            for item in lint_zodiac.lint_payload(p, BLACKLIST)
        ]
        self.assertNotIn("voice.adjacent_slides_same_opening_signature", rules)

        repeated = self.rules("Bạn kể chuyện buồn.", "Họ kể chuyện khác.")
        self.assertIn("voice.adjacent_slides_same_opening_signature", repeated)

    def test_paired_construction_counts_per_sentence_not_across_slides(self):
        one = "Họ không chỉ nghe chuyện xảy ra mà còn hỏi lại."
        self.assertNotIn(
            "voice.khong_chi_ma_con_over_1_per_post",
            self.rules(one),
        )
        twice = self.rules(one, one)
        self.assertIn("voice.khong_chi_ma_con_over_1_per_post", twice)

        split = self.rules("Không chỉ vậy.", "Mà còn một chuyện khác.")
        self.assertNotIn("voice.khong_chi_ma_con_over_1_per_post", split)

    def test_schema_validation_is_separate_from_voice_lint(self):
        p = payload("Sự chú ý nằm ở đây.")
        p["debug"] = True
        voice_rules = [
            item["rule"] for item in lint_zodiac.lint_payload(p, BLACKLIST)
        ]
        schema_rules = [
            item["rule"] for item in lint_zodiac.validate_payload_schema(p)
        ]
        self.assertTrue(any(rule.startswith("voice.blacklist:") for rule in voice_rules))
        self.assertIn("schema.top_level_must_only_contain_ideas", schema_rules)

    def test_blacklist_file_is_canonical_for_tests_and_matches_rule(self):
        raw = BLACKLIST_PATH.read_text(encoding="utf-8")
        self.assertNotIn("# Zodiac v9 prose blacklist", BLACKLIST)
        self.assertTrue(all(not item.startswith("#") for item in BLACKLIST))

        rule = RULE_PATH.read_text(encoding="utf-8")
        match = re.search(r"\*\*BLACKLIST trong prose:\*\*\s*([^\n]+)", rule)
        self.assertIsNotNone(match)
        rule_terms = re.findall(r"`([^`]+)`", match.group(1))
        self.assertEqual(rule_terms, BLACKLIST)

    def test_cli_exit_codes_and_json_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good_path = root / "good.json"
            bad_path = root / "bad.json"
            good_path.write_text(
                json.dumps(payload("Thấy một điểm hay là khen đúng điểm đó."), ensure_ascii=False),
                encoding="utf-8",
            )
            bad_path.write_text(
                json.dumps(payload("Tóm lại, đây là dấu hiệu rõ nhất."), ensure_ascii=False),
                encoding="utf-8",
            )

            good = subprocess.run(
                [sys.executable, str(LINT_PATH), str(good_path), "--blacklist", str(BLACKLIST_PATH)],
                check=False,
                capture_output=True,
                text=True,
            )
            bad = subprocess.run(
                [sys.executable, str(LINT_PATH), str(bad_path), "--blacklist", str(BLACKLIST_PATH)],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(good.returncode, 0)
            self.assertEqual(json.loads(good.stdout), [])
            self.assertEqual(bad.returncode, 1)
            self.assertTrue(json.loads(bad.stdout))


if __name__ == "__main__":
    unittest.main()
