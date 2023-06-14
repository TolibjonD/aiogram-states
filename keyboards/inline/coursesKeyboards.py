from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

coursesBtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🖥 Xizmatlar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books")
        ],
        [
            InlineKeyboardButton(text="🕸 Web sahifani ko'rish", url="http://tolibjondv.pythonanywhere.com/")
        ],
        [
            InlineKeyboardButton(text="🔍 Qidiruv", switch_inline_query_current_chat="")
        ],
        [
            InlineKeyboardButton(text="🍪 Ulashish", switch_inline_query="Oliy ta'limdagi muammolarga yechim.")
        ]
    ],
)