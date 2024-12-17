import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_open_json(path: str) -> list | Any:
    """Функция получения данных из json файла"""
    try:
        logger.info("Открытие файла по заданному пути")
        with open(path, encoding="utf-8") as file:
            try:
                logger.info("Преобразование данных из файла в python объект")
                data_json = json.load(file)
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка декорирования: {ex}")
                print("Ошибка преобразования данных")
                return []
        return data_json
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        print("Файл не найден")
        return []


if __name__ == "__main__":
    path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    data = get_open_json(path_to_file)
    print(data)
    print(type(data))
