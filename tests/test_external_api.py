import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


@patch("requests.get")
def test_get_transaction_amount_rub_currency(mock_get):
    mock_get.return_value = {"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}
    assert get_transaction_amount({"operationAmount": {"amount": 1, "currency": {"code": "RUB"}}}) == 1


@patch("requests.get")
def test_get_transaction_amount_usd_currency(mock_get):
    transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 103.854485}
    assert get_transaction_amount(transaction) == 103.854
    mock_get.assert_called_once_with(
        url, headers={"apikey": API_KEY}, params={"amount": "1", "from": "USD", "to": "RUB"}
    )
