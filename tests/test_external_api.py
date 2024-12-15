from unittest.mock import patch
import requests
from src.external_api import get_transaction_amount
import pytest


@pytest.fixture
def transaction():
    return {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
          "amount": "1",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
      }

@patch("requests.get")
def test_get_transaction_amount_rub_currency(mock_get):
    mock_get.return_value = {"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}
    assert get_transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1


@patch("requests.get")
def test_get_transaction_amount_usd_currency(mock_get):
    mock_get.return_value.json.return_value = {
                                              "date": "2018-02-22",
                                              "historical": "",
                                              "info": {
                                                "rate": 148.972231,
                                                "timestamp": 1519328414
                                              },
                                              "query": {
                                                "amount": 1,
                                                "from": "USD",
                                                "to": "RUB"
                                              },
                                              "result": 104.461,
                                              "success": true
                                            }
    assert get_transaction_amount(transaction) == 104.461
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert")
