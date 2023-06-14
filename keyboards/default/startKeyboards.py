from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

startBtn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 Ta'lim"),
            KeyboardButton("📒 Qo'llanma")
        ],
    ],
    resize_keyboard=True
)