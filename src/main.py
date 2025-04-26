import os

from src.csv_xlsx import get_open_csv, get_open_xlsx
from src.filtering import filter_operations
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_open_json
from src.widget import get_data, mask_account_card

path_to_file_csv = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
path_to_file_xlsx = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")
path_to_file_json = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def main() -> None:
    """Функция связывающая все функциональности проекта"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice_user = input("Пользователь: ")

    # пользователь выбирает из какого файла обработать информацию, обработка выбранного формата
    while True:

        if choice_user == "1":
            print("Для обработки выбран JSON-файл")
            list_data = get_open_json(path_to_file_json)  # обработка файла json
            # print(list_data)
            break
        elif choice_user == "2":
            print("Для обработки выбран CSV-файл")
            list_data = get_open_csv(path_to_file_csv)  # обработка файла csv
            # print(list_data)
            break
        elif choice_user == "3":
            print("Для обработки выбран XLSX-файл")
            list_data = get_open_xlsx(path_to_file_xlsx)  # обработка файла xlxs
            # print(list_data)
            break
        else:
            choice_user = input("Пользователь: ")

    # выбор фильтрации по статусу транзакции
    while True:

        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING" "")
        available_status = {"EXECUTED", "CANCELED", "PENDING"}
        input_status = input()
        status = input_status.upper()

        if status in available_status:
            print(f"Операции отфильтрованы по статусу {status}")
            sort_transaction_on_status = filter_by_state(list_data, status)
            # print(sort_transaction_on_status)
            break
        else:
            print(f"Статус операции {status} недоступен.")

    # сортировка по дате
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            # сортировка по убыванию даты или по возрастанию
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                user_input = input().lower()
                if user_input == "по возрастанию":
                    sort_ascending = False
                    sort_transactions_date = sort_by_date(sort_transaction_on_status, sort_ascending)
                    # print(sort_transactions_date)
                    break
                elif user_input == "по убыванию":
                    sort_ascending = True
                    sort_transactions_date = sort_by_date(sort_transaction_on_status, sort_ascending)
                    # print(sort_transactions_date)
                    break
                else:
                    print("Неверный ввод")
            break
        elif user_input == "нет":
            sort_transactions_date = sort_transaction_on_status
            break
        else:
            print("Неверный ввод")

    # фильтрация транзакций по валюте
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            filter_currency = "RUB"
            iterator_currency = filter_by_currency(sort_transactions_date, filter_currency)
            final_data_on_currency = list(iterator_currency)
            # print(final_data_on_currency)
            break
        elif user_input == "нет":
            final_data_on_currency = sort_transactions_date
            # print(final_data_on_currency)
            break
        else:
            print("Неверный ввод")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            print("Введите ключевое слово")
            user_input = input()
            filter_data_on_description = filter_operations(final_data_on_currency, user_input)
            # print(filter_data_on_description)
            break
        elif user_input == "нет":
            filter_data_on_description = final_data_on_currency
            # print(filter_data_on_description)
            break
        else:
            print("Неверный ввод")

    # функция вывода информации пользователю
    def print_transaction(list_transaction: list[dict]) -> None:
        """Вывод информации пользователю по транзакциям"""
        if not list_transaction:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            return

        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(list_transaction)}\n")

        for transaction in list_transaction:
            date = get_data(transaction["date"])
            description = transaction.get("description")
            if "operationAmount" in transaction:
                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["name"]
            else:
                amount = transaction["amount"]
                currency = transaction.get("currency_code")

            if "from" in transaction and transaction["from"]:
                transaction_from = mask_account_card(transaction["from"])
            else:
                transaction_from = ""

            if "to" in transaction:
                transaction_to = mask_account_card(transaction["to"])
            else:
                transaction_to = ""

            print(f"{date} {description}")
            if transaction_from and transaction_to:
                print(f"{transaction_from} -> {transaction_to}")

            elif transaction_to:
                print(f"{transaction_to}")
            print(f"Сумма: {amount} {currency}\n")

    print("\n" + "=" * 50)
    print_transaction(filter_data_on_description)

    # if counter_transaction == 0:
    #     print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    # else:
    #     print("Распечатываю итоговый список транзакций...")
    #     print(f"Всего банковских операций в выборке: {counter_transaction}")

    # print(transaction)

    # if counter_transaction == 0:
    #     print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    # else:
    #     print("Распечатываю итоговый список транзакций...")
    #     print(f"Всего банковских операций в выборке: {counter_transaction}")
    #
    #     print(f"{date} {description}")
    #     print(f"{transaction_to} -> {transaction_from}")
    #     print(f"Сумма: {sum_of_transaction}")
    #     print()


# if __name__ == "__main__":
#     main()
