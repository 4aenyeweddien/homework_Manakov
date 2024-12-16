import os
import requests
from dotenv import load_dotenv
from unittest.mock import patch

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def get_transaction_amount(transaction: dict) -> float:
    """функция конвертации валюты"""
    amount = 0
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount_transaction = transaction["operationAmount"]["amount"]
    if currency_code != "RUB":
        try:
            payload = {
                "amount": f"{amount_transaction}",
                "from": f"{currency_code}",
                "to": "RUB"
            }

            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            if status_code == 200:
                data_json = response.json()
                amount += data_json["result"]
                return round(amount, 3)
            else:
                print(status_code)
                print(f"Запрос не был успешным. Возможная причина: {response.reason}")
        except requests.exceptions.RequestException:
            print("Ошибка конвертации")

    else:
        amount += float(transaction["operationAmount"]["amount"])
        return amount


# if __name__ == "__main__":
#     transaction = {
#         "id": 207126257,
#         "state": "EXECUTED",
#         "date": "2019-07-15T11:47:40.496961",
#         "operationAmount": {
#           "amount": "1",
#           "currency": {
#             "name": "USD",
#             "code": "USD"
#           }
#         },
#         "description": "Открытие вклада",
#         "to": "Счет 35737585785074382265"
#       }
# transaction_amount = get_transaction_amount(transaction)
# print(transaction_amount)


# payload = {
#     "amount": "1200",
#     "from": "USD",
#     "to": "RUB"
# }
#
# headers = {
#   "apikey": f"{API_KEY}"
# }
#
# response = requests.get(url, headers=headers, params=payload)
#
# status_code = response.status_code
# result = response.text
#
# data_json = response.json()
# print(type(data_json))
# print(data_json["result"])