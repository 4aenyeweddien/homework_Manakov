import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# @pytest.mark.parametrize("filter, extended", )
# def test_filter_by_currency(transaction, filter):
#     """"""
#     filter_transaction = (x for x in transaction if x["operationAmount"]["currency"]["code"] == filter)
#     assert next(filter_by_currency(transaction, filter)) == filter_transaction


def test_filter_by_currency_usd(transaction):
    """тест на фильрацию валют по значению USD"""
    generator = filter_by_currency(transaction, filter_transaction="USD")
    assert next(generator) == {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }
    assert next(generator) == {
                                "id": 142264268,
                                "state": "EXECUTED",
                                "date": "2019-04-04T23:20:05.206878",
                                "operationAmount": {
                                    "amount": "79114.93",
                                    "currency": {
                                        "name": "USD",
                                        "code": "USD"
                                    }
                                },
                                "description": "Перевод со счета на счет",
                                "from": "Счет 19708645243227258542",
                                "to": "Счет 75651667383060284188"
                                }
    assert next(generator) == {
                                "id": 895315941,
                                "state": "EXECUTED",
                                "date": "2018-08-19T04:27:37.904916",
                                "operationAmount": {
                                    "amount": "56883.54",
                                    "currency": {
                                        "name": "USD",
                                        "code": "USD"
                                    }
                                },
                                "description": "Перевод с карты на карту",
                                "from": "Visa Classic 6831982476737658",
                                "to": "Visa Platinum 8990922113665229"
                                 }
    with pytest.raises(StopIteration):
        assert next(generator)


def test_filter_by_currency_rub(transaction):
    """тест на фильрацию валют по значению RUB"""
    generator = filter_by_currency(transaction, filter_transaction="RUB")
    assert next(generator) == {
                                "id": 873106923,
                                "state": "EXECUTED",
                                "date": "2019-03-23T01:09:46.296404",
                                "operationAmount": {
                                    "amount": "43318.34",
                                    "currency": {
                                        "name": "руб.",
                                        "code": "RUB"
                                    }
                                },
                                "description": "Перевод со счета на счет",
                                "from": "Счет 44812258784861134719",
                                "to": "Счет 74489636417521191160"
                                }
    assert next(generator) == {
                                "id": 594226727,
                                "state": "CANCELED",
                                "date": "2018-09-12T21:27:25.241689",
                                "operationAmount": {
                                    "amount": "67314.70",
                                    "currency": {
                                        "name": "руб.",
                                        "code": "RUB"
                                    }
                                },
                                "description": "Перевод организации",
                                "from": "Visa Platinum 1246377376343588",
                                "to": "Счет 14211924144426031657"
                            }
    with pytest.raises(StopIteration):
        assert next(generator)


def test_filter_by_no_currency(transaction):
    """тест на фильтрацию по некорректной валюте"""
    with pytest.raises(StopIteration):
        generator = filter_by_currency(transaction, filter_transaction="YEN")
        assert next(generator)


def test_filter_by_no_currency_empty(transaction):
    """тест на фильтрацию операций в пустом списке"""
    with pytest.raises(StopIteration):
        generator = filter_by_currency([], filter_transaction="YEN")
        assert next(generator)


def test_transaction_descriptions(transaction):
    """тест на вывод описания карт"""
    generator = transaction_descriptions(transaction)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_empty(transaction):
    """тест на вывод описания карт при пустом списке"""
    with pytest.raises(StopIteration):
        generator = transaction_descriptions([])
        assert next(generator)


def test_card_number_generator():
    """тест генерации карт"""
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"
