from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Фильтрует операции по ключу state"""

    new_list = []

    for key in list_dict:
        if key['state'] == state_id:
            new_list.append(key)
    return new_list


def sort_by_date(list_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Сортирует список словарей по убывванию даты"""
    sorted_list_dict_date = sorted(list_dict, key=lambda list_dict: list_dict['date'], reverse=reverse)
    return sorted_list_dict_date


# if __name__ == '__main__':
#     list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#             {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
#             {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T21:27:25.241689'},
#             {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'}]
#
#     result1 = filter_by_state(list_dict)
#     print(result1)
#     result2 = sort_by_date(list_dict)
#     print(result2)
