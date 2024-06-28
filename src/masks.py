def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает замаскированный номер карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Принимает номер счета и возвращает замескированный номер счета"""

    return f"**{account[-4:]}"


