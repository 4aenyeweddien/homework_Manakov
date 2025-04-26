import re
import os
import collections
from collections import Counter

from src.csv_xlsx import get_open_csv


def filter_operations(transactions_dict: list[dict], search_bar: str) -> list[dict]:
    """Функция фильтрующая список транзакций и возвращает список словарей отфлиртрованных"""
    if not search_bar.strip():
      return []
    else:
        filtered_list = []
        pattern = r"\b" + re.escape(search_bar) + r"\b"
        for transact in transactions_dict:
            if "description" in transact:
                if re.search(pattern, transact["description"], flags=re.IGNORECASE):
                    filtered_list.append(transact)
        return filtered_list


def counting_categories(transactions_dict: list[dict], list_category: list) -> dict:
    """Функция подсчитывает сколько раз совершался транзакция"""

    counting_categories = []
    for transaction in transactions_dict:
        description = transaction.get("description", "")
        for category in list_category:
            pattern = r"\b" + re.escape(category) + r"\b"
            if re.search(pattern, description, flags=re.IGNORECASE):
                counting_categories.append(category)

    counting_transaction = dict(Counter(counting_categories))

    for category in list_category:
        if category not in counting_transaction.keys():
            counting_transaction[category] = 0
    return counting_transaction


if __name__ == "__main__":
    categories_of_operations = ["Перевод с карты на карту", "Перевод организации", "Открытие вклада"]
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
    data = get_open_csv(path_to_file)
    result = counting_categories(data, categories_of_operations)
    print(result)
    # search_user = input()
    # result = filter_operations(data, search_user)
    # print(result)
