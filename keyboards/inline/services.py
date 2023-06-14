from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, programming_callback

serviceMenu = InlineKeyboardMarkup(row_width=1)
dasturlash = InlineKeyboardButton(text="👨🏼‍💻 Dasturlash" , callback_data=course_callback.new(item_name="dasturlash"))

english = InlineKeyboardButton(text="🗽 Ingliz tili", callback_data=course_callback.new(item_name="english"))

model = InlineKeyboardButton(text="🧮 Modellashtirish (MathCad)", callback_data=course_callback.new("model"))

graph = InlineKeyboardButton(text="🔆 Photoshop, CorellDraw, AutoCad", callback_data=course_callback.new("graph"))

math = InlineKeyboardButton(text="📐 Hisoblash tizimlari, Oliy matematika", callback_data=course_callback.new("math"))

serviceMenu.insert(dasturlash)
serviceMenu.insert(english)
serviceMenu.insert(model)
serviceMenu.insert(graph)
serviceMenu.insert(math)

programmingMenu = InlineKeyboardMarkup(row_width=1)
python = InlineKeyboardButton(text="🐍 Python", callback_data=programming_callback.new("python"))
php = InlineKeyboardButton(text="🪖 Php (web, XAMPP)", callback_data=programming_callback.new("php"))
javascript = InlineKeyboardButton(text="🐇 JavaScript (VueJs, NodeJs, NestJs)", callback_data=programming_callback.new("javascript"))
frontend = InlineKeyboardButton(text="🌎 HTML, CSS, Bootstrap , Tailwind, Js, JQuery", callback_data=programming_callback.new("frontend"))
mbbt = InlineKeyboardButton(text="🧩 MBBT (SQL, MySQL, PostgreSQl, Sqlite3, Ms Access)", callback_data=programming_callback.new("mbbt"))
back_btn = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")

programmingMenu.insert(python)
programmingMenu.insert(php)
programmingMenu.insert(javascript)
programmingMenu.insert(frontend)
programmingMenu.insert(mbbt)
programmingMenu.insert(back_btn)