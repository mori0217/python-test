from calculation import Cal


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start class')
        cls.cal = Cal()
        cls.test_file_name = 'test.txt'

    def test_add_num_and_double(self, request):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file = tmpdir.join(self.test_file_name)
        print("test_file={}".format(test_file))
        assert test_file.read() == 'test'
