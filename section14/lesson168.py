import pytest
from calculation import Cal


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start class')
        cls.cal = Cal()

    @classmethod
    def teardown_class(cls):
        print('end class')
        del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
