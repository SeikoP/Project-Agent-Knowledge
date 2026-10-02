from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINT_PATH = ROOT / "tools" / "lint_zodiac.py"
spec = importlib.util.spec_from_file_location("lint_zodiac", LINT_PATH)
lint_zodiac = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(lint_zodiac)

BLACKLIST = [
    "phía họ", "tương tác", "sự chú ý", "kết nối", "cảm nhận rõ",
    "thể hiện", "đón nhận", "điều này cho thấy", "qua đó", "nhìn chung",
    "tóm lại", "vì vậy",
]


def payload(*slides: str) -> dict:
    return {
        "ideas": [{
            "idea_id": 1,
            "slides": [{
                "content_blocks": [{"block_id": "body-1", "type": "body", "text": text}]
            } for text in slides],
        }]
    }


class ZodiacVoiceLintTests(unittest.TestCase):
    def rules(self, *slides: str) -> list[str]:
        return [item["rule"] for item in lint_zodiac.lint_payload(payload(*slides), BLACKLIST)]

    def test_good_cancer_scene_passes(self):
        self.assertEqual(
            self.rules("Nhớ chuyện bạn kể hôm trước. Lần sau gặp còn hỏi: giờ ổn chưa?"),
            [],
        )

    def test_bad_cancer_explanatory_sentence_is_caught(self):
        rules = self.rules(
            "Họ không chỉ nghe chuyện gì xảy ra mà còn để ý xem chuyện đó làm bạn vui hay khó chịu."
        )
        self.assertIn("voice.sentence_over_18_words", rules)

    def test_good_leo_scene_passes(self):
        self.assertEqual(self.rules("Thấy một điểm hay là khen đúng điểm đó."), [])

    def test_bad_leo_bookish_sentence_is_caught(self):
        rules = self.rules("Sư Tử thể hiện sự chú ý thông qua lời khen dành cho người kia.")
        self.assertTrue(any(rule.startswith("voice.blacklist:") for rule in rules))

    def test_good_virgo_scene_passes(self):
        self.assertEqual(self.rules("Nói chuyện chậm rãi. Điều gì nghĩ thật thì nói thật."), [])

    def test_bad_virgo_joined_clause_is_caught(self):
        rules = self.rules("Xử Nữ nói chuyện chân thành nhưng vẫn tiếp cận từ tốn.")
        self.assertIn("voice.banned_clause_connector", rules)

    def test_two_good_examples_still_fail_if_adjacent_opening_repeats(self):
        rules = self.rules(
            "Bạn kể một chuyện buồn. Họ hỏi lại đúng đoạn làm bạn khó chịu.",
            "Bạn muốn giữ chuyện riêng thì họ không gặng hỏi.",
        )
        self.assertIn("voice.adjacent_slides_same_opening", rules)

    def test_paired_construction_twice_in_one_post_is_caught(self):
        bad = "Họ không chỉ nghe chuyện gì xảy ra mà còn để ý xem chuyện đó làm bạn vui hay khó chịu."
        rules = self.rules(bad, bad)
        self.assertIn("voice.khong_chi_ma_con_over_1_per_post", rules)


if __name__ == "__main__":
    unittest.main()
