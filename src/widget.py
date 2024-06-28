from src import masks


def mask_account_card(number_card_account: str) -> str | None:
    """Принимает строку и возвращает замаскированную"""
    if len(number_card_account.split()[-1]) == 16:
        new_account = masks.get_mask_card_number(number_card_account.split()[-1])
        return f"{number_card_account[:-16]}{new_account}"
    else:
        new_card = masks.get_mask_account(number_card_account.split()[-1])
        return f"{number_card_account[:-20]}{new_card}"


def get_data(date: str) -> str:
    """Принимает строку и выводит дату в нужном формате"""
    date_to_edit = date[0:10].split("-")
    new_date = ".".join(date_to_edit[::-1])
    return new_date


user_card = input()
user_date = input()
result_card = mask_account_card(user_card)
result_date = get_data(user_date)
print(result_card)
print(result_date)
