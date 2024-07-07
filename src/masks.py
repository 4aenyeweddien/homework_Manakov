def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает замаскированный номер карты"""
    if len(card_number) != 16:
        raise ValueError("Неверный номер карты")

    if not card_number.isdigit():
        raise ValueError("Недопустимые символы")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Принимает номер счета и возвращает замескированный номер счета"""
    if not account.isdigit():
        raise ValueError("Недопустимые символы")

    if len(account) != 20:
        raise ValueError("Неверный номер счета")

    return f"**{account[-4:]}"


# if __name__ == '__main__':
#     result1 = get_mask_card_number("7000792123606361")
#     print(result1)
#     result2 = get_mask_account("7365410d84asd5874305")
#     print(result2)
