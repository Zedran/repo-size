import unittest

from utils import convert_kb


class TestRepoSize(unittest.TestCase):
    def test_convert_kb(self):
        cases = {
            0:                                    "0.00 KB",
            767:                                "767.00 KB",
            999:                                "999.00 KB",
            1_000:                                "1.00 MB",
            1_001:                                "1.00 MB",
            12_345_678:                          "12.35 GB",
            1_234_567_890_123_456_789_012_345: "1234.57 YB"
        }

        for inp, expected in cases.items():
            self.assertEqual(convert_kb(inp), expected)


if __name__ == "__main__":
    unittest.main()
