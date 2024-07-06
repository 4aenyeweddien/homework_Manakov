from src.widget import mask_account_card, get_data
import pytest


@pytest.mark.parametrize("number, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                              ("Счет 64686473678894779589", "Счет **9589"),
                                              ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                              ("Счет 35383033474447895560", "Счет **5560"),
                                              ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                              ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                              ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                              ("Счет 73654108430135874305", "Счет **4305"),])
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected


@pytest.mark.parametrize("number", [("Maestro 159683786199"),
                                    ("Счет 6468647367779589"),
                                    ("MasterCard 7158300734345726758"),
                                    ("Счет 35383033474434547895560"),
                                    ("Visa Platinum 8990922asd665229"),
                                    ("Visa Gold "),
                                    ("Счет 736541084301asd74305"),])
def test_mask_account_card_invalid(number):
    with pytest.raises(ValueError):
        mask_account_card(number)



def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("number", [("24.03.11T02-26-18"),
                                    ("2024-03-11 02:26:18.671407"),
                                    ("T02:26:18.6714072024-03-11"),
                                    # ("2024-03-11T02:26:18.671407"),
                                    # ("2024-03-11T02:26:18.671407"),
                                    ("T02:26:18.671407"),])
def test_get_data_invalid(number):
    with pytest.raises(ValueError):
        get_data(number)


