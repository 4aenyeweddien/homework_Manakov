import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты и возвращает замаскированный номер карты"""
    logger.info("Ввод номера карты")
    if len(card_number) != 16:
        logger.warning("Введены недопустмсое количество символов карты")
        raise ValueError("Неверный номер карты")
    if not card_number.isdigit():
        logger.warning("Введены недопустимые символы в номере карты")
        raise ValueError("Недопустимые символы")
    logger.info("Вывод преобразованного номера карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Принимает номер счета и возвращает замескированный номер счета"""
    logger.info("Ввод номера счета")
    if not account.isdigit():
        logger.warning("Введены недопустимые символы")
        raise ValueError("Недопустимые символы")
    if len(account) != 20:
        logger.warning("Введено недопустимое количество символов")
        raise ValueError("Неверный номер счета")
    logger.info("Вывод преобразованного номера счета")
    return f"**{account[-4:]}"


# if __name__ == "__main__":
#     result1 = get_mask_card_number("7000792123606361")
#     print(result1)
#     result2 = get_mask_account("73654101841235874305")
#     print(result2)
