import pytest
from calculation import Cal


class TestCal(object):
    def test_add_num_and_double(self):
        cal = Cal()
        assert cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        cal = Cal()
        with pytest.raises(ValueError):
            cal.add_num_and_double('1', '1')
