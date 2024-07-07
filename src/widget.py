from datetime import datetime

from src import masks


def mask_account_card(number_card_account: str) -> str | None:
    """Принимает строку и возвращает замаскированную"""
    if "счет" in number_card_account.lower():
        if len(number_card_account.split()[-1]) == 20 and number_card_account.split()[-1].isdigit():
            new_card = masks.get_mask_account(number_card_account.split()[-1])
            return f"{number_card_account[:-20]}{new_card}"
        else:
            raise ValueError("недопустимый номер счета")
    else:
        if len(number_card_account.split()[-1]) == 16 and number_card_account.split()[-1].isdigit():
            new_account = masks.get_mask_card_number(number_card_account.split()[-1])
            return f"{number_card_account[:-16]}{new_account}"
        else:
            raise ValueError("недопустимый номер карты")
    # if len(number_card_account.split()[-1]) == 16:
    #     new_account = masks.get_mask_card_number(number_card_account.split()[-1])
    #     return f"{number_card_account[:-16]}{new_account}"
    # else:
    #     new_card = masks.get_mask_account(number_card_account.split()[-1])
    #     return f"{number_card_account[:-20]}{new_card}"


def get_data(date: str) -> str:
    """Принимает строку и выводит дату в нужном формате"""
    format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = format_date.strftime("%d.%m.%Y")
    return new_date
    # date_to_edit = date[0:10].split("-")
    # new_date = ".".join(date_to_edit[::-1])
    # return new_date


# if __name__ == "__main__":
#     # user_card = input()
#     user_date = "2024-03-11T02:26:18.671407"
#     # result_card = mask_account_card(user_card)
#     result_date = get_data(user_date)
#     # print(result_card)
#     print(result_date)
