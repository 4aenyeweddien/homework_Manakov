import masks


def mask_account_card(user_input: str) -> str:
    """Принимает строку и возвращает ее замаскированной"""
    if len(user_input.split()[-1]) == 16:
        new_account = masks.get_mask_card_number(user_input.split()[-1])
        disguised_account = f"{user_input[:-16]}{new_account}"
        return disguised_account
    elif len(user_input.split()[-1]) == 20:
        new_card = masks.get_mask_account(user_input.split()[-1])
        disguised_card = f"{user_input[:-20]}{new_card}"
        return disguised_card


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







