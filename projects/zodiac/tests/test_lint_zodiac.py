from __future__ import annotations

import importlib.util
import tempfile
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

    def test_good_cancer_camera_scene_passes(self):
        self.assertEqual(
            self.rules("Nhớ chuyện bạn kể hôm trước. Lần sau gặp còn hỏi: giờ ổn chưa?"),
            [],
        )

    def test_bad_cancer_explanatory_pair_is_caught(self):
        rules = self.rules(
            "Họ không chỉ nghe chuyện xảy ra mà còn để ý xem chuyện đó làm bạn vui hay khó chịu."
        )
        self.assertIn("voice.sentence_over_18_words", rules)

    def test_bad_leo_bookish_word_is_caught(self):
        rules = self.rules("Sư Tử thể hiện sự chú ý qua lời khen.")
        self.assertTrue(any(rule.startswith("voice.blacklist:") for rule in rules))

    def test_good_leo_action_passes(self):
        self.assertEqual(self.rules("Thấy một điểm hay là khen đúng điểm đó."), [])

    def test_good_virgo_privacy_scene_passes(self):
        self.assertEqual(self.rules("Bạn muốn giữ chuyện riêng thì họ không gặng hỏi."), [])

    def test_generalizing_ending_is_caught(self):
        rules = self.rules("Bạn nhắn. Họ trả lời. Vì vậy đây là dấu hiệu rõ nhất.")
        self.assertIn("voice.generalizing_ending", rules)

    def test_adjacent_slides_same_opening_is_caught(self):
        rules = self.rules("Bạn kể chuyện.", "Bạn nhắn trước.")
        self.assertIn("voice.adjacent_slides_same_opening", rules)

    def test_sentence_over_18_words_is_caught(self):
        rules = self.rules(
            "Đang nói chuyện bình thường rồi họ vẫn tiếp tục giải thích rất dài về điều vừa xảy ra trong đoạn chat đó."
        )
        self.assertIn("voice.sentence_over_18_words", rules)


if __name__ == "__main__":
    unittest.main()
