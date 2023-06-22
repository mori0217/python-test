import requests


class ThirdPartyBonusRestApi(object):
    def get_api_name(self):
        return "Bonus Rest Api"

    def bonus_price(self, year):
        # connect to 3rd party vendor and get price
        res = requests.get('http://localhost/bonus', params={'year': year})
        return res.json()['price']


class Salary(object):
    def __init__(self, base=100, year=2023) -> None:
        self.bonus_api = ThirdPartyBonusRestApi()
        self.base = base
        self.year = year

    def calculate_salary(self):
        bonus = 0
        if self.year < 2024:
            bonus = self.bonus_api.bonus_price(self.year)
        return self.base + bonus
