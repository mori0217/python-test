from calculation import Cal


def test_add_num_and_double():
    cal = Cal()
    assert cal.add_num_and_double(1, 1) == 4


class TestCal(object):
    def test_add_num_and_double(self):
        cal = Cal()
        assert cal.add_num_and_double(1, 1) == 4
