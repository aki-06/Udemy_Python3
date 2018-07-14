"""
https://docs.python.jp/3/library/unittest.html
"""

import unittest
import calculation

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        """
        正しく計算がされているか確認するテスト
        """
        cal = calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        """
        ValueErrorが発生するか確認するためのテスト
        """
        cal = calculation.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()