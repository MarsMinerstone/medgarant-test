import unittest
from datetime import time

from medgarant import get_gaps


class TestGetGaps(unittest.TestCase):
    def test_get_gaps(self):
        busy = [
            {'start': '9:00', 'stop': '15:00'},
            {'start': '16:20', 'stop': '17:20'},
            {'start': '19:05', 'stop': '21:00'}
        ]

        expected_gaps = [
            {'start': time(15, 00), 'stop': time(15, 30)},
            {'start': time(15, 30), 'stop': time(16, 00)},
            {'start': time(17, 20), 'stop': time(17, 50)},
            {'start': time(17, 50), 'stop': time(18, 20)},
            {'start': time(18, 20), 'stop': time(18, 50)}
        ]

        gaps = get_gaps(busy)

        self.assertEqual(len(gaps), len(expected_gaps))
        for gap, expected_gap in zip(gaps, expected_gaps):
            self.assertEqual(gap['start'], expected_gap['start'])
            self.assertEqual(gap['stop'], expected_gap['stop'])


if __name__ == '__main__':
    unittest.main()
