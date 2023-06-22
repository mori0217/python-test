from calculation import Cal


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start class')
        cls.cal = Cal()
        cls.test_file_name = 'test.txt'

    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4
