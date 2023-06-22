
import unittest
from unittest.mock import MagicMock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_of_salary(self):
        s = salary.Salary()
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculate_salary(), 101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(2023)
        s.bonus_api.bonus_price.assert_called_once_with(2023)

    def test_calculation_of_salary_with_no_bonus(self):
        s = salary.Salary(year=2024)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculate_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()
