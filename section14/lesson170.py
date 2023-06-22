from calculation import Cal

is_release = True


class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start class')
        cls.cal = Cal()

    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print("os_name={}".format(os_name))
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4
