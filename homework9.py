
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://bank.gov.ua/ua/markets/exchangerates/'
r = requests.get(URL)

html = bs(r.text, "html.parser")
table = html.find_all('td')
for i in table:
    print(i.text)
class Convertor:
    def __init__(self,amount, USD, valute):
        self.amount = amount
        self.USD = USD
        self.valute = valute

    def convert_to_usd(self):
        try:
            valute = int(input('Введіть валюту своєї країни grn/EUR:'))
            amount = int(input('Виберіть кількість вашої валюти яку ви хочете переробити в амереканські долари:'))
            if valute == 1:
                USD = amount / 37,6194
                print('Доларів', USD)
            else:
                print('Неможливо знайти курс для введеної валюти.')
        except ValueError:
            print("Некоректне введення кількості валюти.")
converter = Convertor(100, 2, 1)
converter.convert_to_usd()







