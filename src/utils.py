import json
import os

path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_open_json(path: str) -> list:
    """Функция получения данных из json файла"""
    try:
        with open(path, encoding='utf-8') as file:
            try:
                data_json = json.load(file)
            except json.JSONDecodeError:
                print("Ошибка преобразования данных")
                return []
        return data_json
    except FileNotFoundError:
        print("Файл не найден")
        return []


# if __name__ == "__main__":
#     path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
#     data = get_open_json(path_to_file)
#     print(data)
#     print(type(data))

