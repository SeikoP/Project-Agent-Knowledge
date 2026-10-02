from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import re
import tempfile
import unicodedata
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINT_PATH = ROOT / "tools" / "lint_zodiac.py"
RULE_PATH = ROOT / "rules" / "content-design.md"
BLACKLIST_PATH = ROOT / "tools" / "blacklist.txt"

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
                "content_blocks": [{"block_id": "body-1", "type": "body", "text": text}]
            } for text in slides],
        }]
    }


def payload_blocks(*slides: list[dict[str, str]]) -> dict:
    return {
        "ideas": [{
            "idea_id": 1,
            "slides": [{"content_blocks": blocks} for blocks in slides],
        }]
    }


class ZodiacVoiceLintTests(unittest.TestCase):
    def rules(self, *slides: str) -> list[str]:
        return [item["rule"] for item in lint_zodiac.lint_payload(payload(*slides), BLACKLIST)]

    def test_good_cancer_scene_passes(self):
        self.assertEqual(
            self.rules("Chuyện bạn kể hôm trước, họ nhớ á. Lần sau gặp là hỏi: chuyện đó ổn chưa?"),
            [],
        )

    def test_sentence_over_24_syllables_is_caught(self):
        rules = self.rules(
            "Họ nghe bạn kể chuyện rồi hỏi thêm từng chi tiết để hiểu rõ hơn trước khi hai người nói sang chuyện khác, rồi vẫn cố giải thích tiếp cho thật đầy đủ."
        )
        self.assertIn("voice.sentence_over_24_syllables", rules)

    def test_good_leo_scene_passes(self):
        self.assertEqual(self.rules("Thấy bạn có điểm hay là khen liền."), [])

    def test_bad_leo_bookish_sentence_is_caught(self):
        rules = self.rules("Sư Tử thể hiện sự chú ý thông qua lời khen dành cho người kia.")
        self.assertTrue(any(rule.startswith("voice.blacklist:") for rule in rules))

    def test_report_like_chat_phrases_are_caught(self):
        cases = {
            "Cuộc chat tự nhiên im.": "voice.blacklist:cuộc chat",
            "Không có câu chốt.": "voice.blacklist:câu chốt",
            "Họ chuyển sang mục tiêu khác.": "voice.blacklist:chuyển sang mục tiêu khác",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertIn(expected, self.rules(text))

    def test_good_virgo_scenes_pass(self):
        self.assertEqual(self.rules("Họ nói chuyện từ từ. Mà nghĩ sao nói vậy hà."), [])
        self.assertEqual(self.rules("Bạn không muốn kể là họ thôi, không hỏi nữa luôn."), [])

    def test_banned_connectors_are_caught(self):
        for connector in ("trong khi", "trong lúc"):
            with self.subTest(connector=connector):
                self.assertIn(
                    "voice.banned_clause_connector",
                    self.rules(f"Họ nghe {connector} bạn vẫn đang nói."),
                )

    def test_nhung_is_allowed_for_natural_contrast(self):
        self.assertNotIn(
            "voice.banned_clause_connector",
            self.rules("Họ vẫn trả lời, nhưng không mở chuyện trước."),
        )

    def test_adjacent_opening_uses_two_words_after_pronoun(self):
        rules = self.rules("Bạn nhắn trước.", "Bạn kể chuyện.")
        self.assertNotIn("voice.adjacent_slides_same_opening", rules)
        rules = self.rules("Bạn nhắn trước.", "Họ nhắn trước.")
        self.assertIn("voice.adjacent_slides_same_opening", rules)

    def test_headline_is_not_linted_but_callout_is(self):
        data = payload_blocks(
            [
                {"block_id": "headline-1", "type": "headline", "text": "Họ tương tác rất nhiều"},
                {"block_id": "body-1", "type": "body", "text": "Bạn nhắn trước."},
            ],
            [
                {"block_id": "callout-1", "type": "callout", "text": "Họ tương tác."},
            ],
        )
        errors = lint_zodiac.lint_payload(data, BLACKLIST)
        rules = [item["rule"] for item in errors]
        self.assertEqual(sum(rule == "voice.blacklist:tương tác" for rule in rules), 1)
        self.assertNotIn("voice.adjacent_slides_same_opening", rules)

    def test_paired_construction_twice_in_one_post_is_caught(self):
        first = "Họ không chỉ nghe mà còn hỏi lại."
        second = "Bạn không chỉ kể mà còn nói rõ hơn."
        rules = self.rules(first, second)
        self.assertIn("voice.khong_chi_ma_con_over_1_per_post", rules)

        first = "Họ không phải im mà là đang nghe."
        second = "Bạn không phải đoán mà là hỏi thẳng."
        rules = self.rules(first, second)
        self.assertIn("voice.khong_phai_ma_la_over_1_per_post", rules)

    def test_paired_construction_does_not_join_across_slides(self):
        rules = self.rules("Họ không chỉ nghe chuyện.", "Mà còn hỏi lại.")
        self.assertFalse(any("khong_chi_ma_con" in rule for rule in rules))

    def test_nfd_input_matches_nfc_blacklist(self):
        nfd = unicodedata.normalize("NFD", "Họ phản hồi rất nhanh.")
        self.assertIn("voice.blacklist:phản hồi", self.rules(nfd))

    def test_blacklist_matches_word_boundaries(self):
        self.assertIn("voice.blacklist:phản hồi", self.rules("Họ phản hồi."))
        self.assertNotIn("voice.blacklist:phản hồi", self.rules("Họ phản hồix."))

    def test_generalization_and_blacklist_are_deduplicated_for_same_sentence(self):
        rules = self.rules("Tóm lại, họ trả lời.")
        relevant = [
            rule for rule in rules
            if rule == "voice.generalizing_ending" or rule == "voice.blacklist:tóm lại"
        ]
        self.assertEqual(len(relevant), 1)

    def test_hedge_opener_kieu_is_caught(self):
        self.assertIn("voice.hedge_opener", self.rules("Kiểu họ nhắn trước."))

    def test_fillers_count_only_at_sentence_or_clause_end(self):
        self.assertEqual(self.rules("Họ luôn nói thật. Rồi làm liền mạch."), [])
        self.assertEqual(self.rules("Họ khen bạn liền."), [])
        self.assertIn(
            "voice.filler_over_1_per_slide",
            self.rules("Họ khen bạn liền, đúng nha."),
        )

    def test_same_filler_cannot_repeat_on_adjacent_slides(self):
        rules = self.rules("Thấy hay là khen liền.", "Nghe xong là trả lời liền.")
        self.assertIn("voice.filler_repeated_adjacent:liền", rules)

    def test_post_filler_cap(self):
        rules = self.rules(
            "Chuyện đó ổn á.",
            "Nói rõ hơn nha.",
            "Nghe cũng ghê.",
            "Vậy là xong hà.",
        )
        self.assertIn("voice.filler_over_3_per_post", rules)

    def test_extra_top_level_keys_are_ignored_but_ideas_is_required(self):
        data = payload("Họ trả lời.")
        data["meta"] = {"source": "fixture"}
        self.assertEqual(lint_zodiac.lint_payload(data, BLACKLIST), [])
        rules = [e["rule"] for e in lint_zodiac.lint_payload({"meta": {}}, BLACKLIST)]
        self.assertEqual(rules, ["schema.ideas_required"])

    def test_error_shape_uses_sentence_key(self):
        error = lint_zodiac.lint_payload(payload("Họ tương tác."), BLACKLIST)[0]
        self.assertIn("sentence", error)
        self.assertNotIn("câu", error)

    def test_load_blacklist_skips_comments_blank_lines_and_normalizes_nfc(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "blacklist.txt"
            path.write_text(
                "# comment\n\n" + unicodedata.normalize("NFD", "phản hồi") + "\n",
                encoding="utf-8",
            )
            self.assertEqual(lint_zodiac.load_blacklist(path), ["phản hồi"])

    def test_blacklist_rule_summary_stays_in_sync(self):
        rule_text = RULE_PATH.read_text(encoding="utf-8")
        match = re.search(
            r"\*\*BLACKLIST trong prose[^\n]*\*\*:\s*\n([^\n]+)",
            rule_text,
        )
        self.assertIsNotNone(match)
        md_terms = set(re.findall(r"`([^`]+)`", match.group(1)))
        self.assertEqual(set(BLACKLIST), md_terms)

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            good = Path(d) / "good.json"
            bad = Path(d) / "bad.json"
            missing = Path(d) / "missing.json"
            good.write_text(json.dumps(payload("Họ trả lời."), ensure_ascii=False), encoding="utf-8")
            bad.write_text(json.dumps(payload("Họ tương tác."), ensure_ascii=False), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(lint_zodiac.main([str(good)]), 0)
                self.assertEqual(lint_zodiac.main([str(bad)]), 1)
                self.assertEqual(lint_zodiac.main([str(missing)]), 2)


if __name__ == "__main__":
    unittest.main()
