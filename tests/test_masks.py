import pytest

from src.masks import get_mask_account, get_mask_card_number


# тесты функции карты
def test_get_mask_card_number(card):
    """тест на маскировку карты"""
    assert get_mask_card_number(card) == "7000 79** **** 6361"


def test_get_mask_card_invalid_number():
    """тест на меньшее количество символов карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("70007922896")


def test_get_mask_card_big_number():
    """тест на превышение количества символов карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("700079228960636112315")


def test_get_mask_card_zero_number():
    """тест на отсутствие символов карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_wrong_card():
    """тест на недопустимые символы карты"""
    with pytest.raises(ValueError):
        get_mask_card_number("7000792asd606361")


# тесты функции счета
def test_get_mask_account(account_number):
    """тест на маскировку счета"""
    assert get_mask_account(account_number) == "**4305"


def test_get_mask_invalid_account_zero():
    """тест на отсутствие символов счета"""
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_invalid_account():
    """тест на превышение количества символов счета"""
    with pytest.raises(ValueError):
        get_mask_account("7365410843013587430512325")


def test_get_mask_invalid_account_small():
    """тест на меньшее количество символов счета"""
    with pytest.raises(ValueError):
        get_mask_account("73654108430")


def test_get_mask_account_wrong():
    """тест на недопустимые символы карты"""
    with pytest.raises(ValueError):
        get_mask_account("7365410d84asd5874305")
