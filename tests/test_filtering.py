import pytest
from src.filtering import filter_operations, counting_categories

SAMPLE_TRANSACTIONS = [
    {"description": "Перевод с карты на счет"},
    {"description": "Перевод со счета на счет"},
    {"description": "Открытие вклада"},
    {"description": "Перевод организации"},
    {"description": "Перевод с карты на карту"},
    {"description": "Перевод организации за услуги"},
]

CATEGORIES = ["Перевод", "Открытие вклада", "Пополнение"]


# Тесты для filter_operations
def test_filter_operations_keyword_match():
    result = filter_operations(SAMPLE_TRANSACTIONS, "Перевод")
    assert len(result) == 5


def test_filter_operations_specific_transfer_type():
    result = filter_operations(SAMPLE_TRANSACTIONS, "Перевод организации")
    assert len(result) == 2
    assert all("Перевод организации" in t["description"] for t in result)


def test_filter_operations_empty_search():
    result = filter_operations(SAMPLE_TRANSACTIONS, "   ")
    assert result == []


def test_filter_operations_no_match():
    result = filter_operations(SAMPLE_TRANSACTIONS, "Кредит")
    assert result == []


# Тесты для counting_categories
def test_counting_categories_basic():
    result = counting_categories(SAMPLE_TRANSACTIONS, CATEGORIES)
    assert result["Перевод"] == 5
    assert result["Открытие вклада"] == 1
    assert result["Пополнение"] == 0


def test_counting_categories_missing_category():
    result = counting_categories(SAMPLE_TRANSACTIONS, CATEGORIES + ["Кредит"])
    assert result["Кредит"] == 0


def test_counting_categories_case_insensitive():
    modified_transactions = SAMPLE_TRANSACTIONS + [
        {"description": "перевод на телефон"}
    ]
    result = counting_categories(modified_transactions, CATEGORIES)
    assert result["Перевод"] == 6