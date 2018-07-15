import os
import pytest
import subprocess

import calculation

class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('test start')
        cls.cal = calculation.Cal()
        subprocess.call('cp -p test.txt test2.txt', shell=True)

    @classmethod
    def teardown_class(cls):
        del cls.cal
        file = './test2.txt'
        if os.path.exists(file):
            subprocess.call('rm -f test2.txt', shell=True)
            print('{}を削除しました'.format(file))
        print('test end')

    def setup_method(self, method):
        print('method{}'.format(method.__name__))

    def teardown_method(self, method):
        print('method{}'.format(method.__name__))


    def test_add_num_and_double(self):
        # cal = calculation.Cal()
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            # cal = calculation.Cal()
            assert self.cal.add_num_and_double('1', '1')