import unittest
from calculation import Cal


class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)


if __name__ == '__main__':
    unittest.main()
