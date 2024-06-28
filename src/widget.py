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




#
# user = input()
# result = mask_account_card(user)
# print(result)
#
#
#
#
#
# # def get_data():
# #     """Принимает строку и выводит дату"""

