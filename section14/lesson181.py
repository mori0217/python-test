import unittest
from unittest import mock
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

    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_of_salary_patch(self, mock_bonus_price):
        mock_bonus_price.return_value = 1

        s = salary.Salary()
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus_price.assert_called()

    def test_calculation_of_salary_patch_with(self):
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus_price:
            mock_bonus_price.return_value = 1

            s = salary.Salary()
            salary_price = s.calculate_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus_price.assert_called()

    def setUp(self):
        self.mock_bonus_price_patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus_price = self.mock_bonus_price_patcher.start()

    def tearDown(self):
        self.mock_bonus_price_patcher.stop()

    def test_calculation_of_salary_patch_patcher(self):
        self.mock_bonus_price.return_value = 1

        s = salary.Salary()
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus_price.assert_called()

    def test_calculation_of_salary_patch_side_effect(self):
        # def side_effect(year):
        # return year * 2
        # self.mock_bonus_price.side_effect = side_effect
        # self.mock_bonus_price.side_effect = lambda year: year * 2
        self.mock_bonus_price.side_effect = [
            1,
            2,
            3,
            ValueError('Bankrupt!!!')]

        s = salary.Salary()

        salary_price = s.calculate_salary()
        self.assertEqual(salary_price, 101)
        self.mock_bonus_price.assert_called()

        salary_price = s.calculate_salary()
        self.assertEqual(salary_price, 102)
        self.mock_bonus_price.assert_called()

        salary_price = s.calculate_salary()
        self.assertEqual(salary_price, 103)
        self.mock_bonus_price.assert_called()

        with self.assertRaises(ValueError):
            salary_price = s.calculate_salary()
