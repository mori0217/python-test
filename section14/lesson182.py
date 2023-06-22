import unittest
from unittest import mock

import salary


class TestSalary(unittest.TestCase):
    @mock.patch('salary.ThirdPartyBonusRestApi', spec=True)
    def test_calculation_of_salary_class(self, mock_rest):
        mock_rest = mock_rest.return_value
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'mock Bonus Rest Api'

        s = salary.Salary()
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()
