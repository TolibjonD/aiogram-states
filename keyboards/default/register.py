from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kontaktni yuborish", request_contact=True)
        ],
    ],
    resize_keyboard=True,
)