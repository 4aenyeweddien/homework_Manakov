from typing import Generator


def filter_by_currency(transaction: list[dict], filter_transaction: str) -> Generator:
    """создает итератор по списку словарей и выводит поочередно операции с указанной валютой"""
    for operation in transaction:
        if operation["operationAmount"]["currency"]["code"] == filter_transaction:
            yield operation
    # filter_transact = filter(lambda x: x["operationAmount"]["currency"]["code"] == filter_transaction, transaction)
    # return filter_transact


def transaction_descriptions(transaction: list[dict]) -> Generator:
    """выводит описание операций"""
    for operation in transaction:
        yield operation["description"]


def card_number_generator(a: int, b: int) -> Generator:
    """генерирует номера карт в заданном диапозоне"""
    for number in range(a, b + 1):
        number_str = str(number)
        while len(number_str) < 16:
            number_str = "0" + number_str
        create_card = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield create_card


# if __name__ == '__main__':
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for _ in range(2):
#         print(next(usd_transactions))
#
#     # descriptions = transaction_descriptions(transactions)
#     # for _ in range(5):
#     #     print(next(descriptions))
#
#     for card_number in card_number_generator(1, 5):
#         print(card_number)
