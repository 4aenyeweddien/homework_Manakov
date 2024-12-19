import csv
from typing import Any

import pandas as pd


def get_open_csv(path: str) -> list:
    """Преобразует данные из csv файла в список словарей"""
    list_transactions = []
    with open(path, "r", encoding="utf-8") as file:
        data_csv = csv.DictReader(file, delimiter=";")
        for row in data_csv:
            list_transactions.append(row)
        return list_transactions


def get_open_xlsx(path: str) -> list | Any:
    """Преобразует данные из excell файла в список словарей"""
    excel_data = pd.read_excel(path)
    df = excel_data.to_dict(orient="records")
    return df


# if __name__ == "__main__":
#     path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
#     data = get_open_csv(path_to_file)
#     print(data)
#     print(type(data))
#
#     path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
#     data = get_open_xlsx(path_to_file)
#     print(data)
#     print(type(data))
