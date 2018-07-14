# pytest

"""
https://docs.pytest.org/en/latest/
"""
import pytest

import calculation

is_release = True

# def test_add_num_and_double():
#     cal = calculation.Cal()
#     assert cal.add_num_and_double(1, 1) == 4

# classで書く場合
class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setup_method(self, method):
        print('method{}'.format(method.__name__))

    def tear_down(self, method):
        print('method{}'.format(method.__name__))

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    @pytest.mark.skipif(is_release==False, reason='skip!!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            assert self.cal.add_num_and_double('1', '1')