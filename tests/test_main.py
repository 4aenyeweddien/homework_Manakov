import pytest
from datetime import datetime
from main import get_data, mask_account_card, filter_by_state, sort_by_date
from src.widget import get_data as widget_get_data
from src.processing import filter_by_state as processing_filter_by_state
from src.processing import sort_by_date as processing_sort_by_date


# Фикстуры с тестовыми данными
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "CANCELED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    ]


# Тесты для функции get_data
def test_get_data():
    assert get_data("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert get_data("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert get_data("2018-06-30T02:08:58.425572") == "30.06.2018"


# Тесты для функции mask_account_card
def test_mask_account_card():
    assert mask_account_card("Visa Platinum 2256483756542539") == "Visa Platinum 2256 48** **** 2539"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert mask_account_card("Счет 78808375133947439319") == "Счет **9319"
    assert mask_account_card("") == ""


# Тесты для фильтрации по статусу
def test_filter_by_state(sample_transactions):
    executed = filter_by_state(sample_transactions, "EXECUTED")
    assert len(executed) == 3
    assert all(t["state"] == "EXECUTED" for t in executed)

    canceled = filter_by_state(sample_transactions, "CANCELED")
    assert len(canceled) == 1
    assert all(t["state"] == "CANCELED" for t in canceled)


# Тесты для сортировки по дате
def test_sort_by_date(sample_transactions):
    sorted_asc = sort_by_date(sample_transactions, True)
    dates = [t["date"] for t in sorted_asc]
    assert dates == sorted(dates)

    sorted_desc = sort_by_date(sample_transactions, False)
    dates = [t["date"] for t in sorted_desc]
    assert dates == sorted(dates, reverse=True)


# Тест для пустого списка транзакций
def test_empty_transactions():
    from main import print_transaction
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        print_transaction([])

    output = f.getvalue()
    assert "Не найдено ни одной транзакции" in output


# Тест вывода транзакции
def test_print_transaction(capsys, sample_transactions):
    from main import print_transaction

    print_transaction([sample_transactions[0]])
    captured = capsys.readouterr()

    assert "26.08.2019 Перевод организации" in captured.out
    assert "Visa Platinum 2256 48** **** 2539 -> Счет **9319" in captured.out
    assert "Сумма: 31957.58 руб." in captured.out