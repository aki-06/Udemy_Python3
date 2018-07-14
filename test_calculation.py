"""
https://docs.python.jp/3/library/unittest.html
"""

import unittest
import calculation

release_name = 'lesson2'

class CalTest(unittest.TestCase):
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    # @unittest.skip('skip')
    @unittest.skipIf(release_name=='lesson', 'skip!!')
    def test_add_num_and_double(self):
        """
        正しく計算がされているか確認するテスト
        """
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        """
        ValueErrorが発生するか確認するためのテスト
        - 例外処理のテストをするときはwithを使う
        """
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()