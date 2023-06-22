import unittest
from unittest.mock import MagicMock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_of_salary(self):
        s = salary.Salary()
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculate_salary(), 101)
