from keyboards.inline.coursesKeyboards import coursesBtn
from keyboards.inline.services import serviceMenu, programmingMenu
from keyboards.inline.callback_data import programming_callback, course_callback
import pytz
from datetime import datetime as dt

from loader import dp
from aiogram import types
tz = pytz.timezone('Asia/Tashkent')

@dp.message_handler(text_contains="Ta'lim")
async def select_category(msg: types.Message):
    await msg.answer("Kerakli bo'limni tanglang", reply_markup=coursesBtn)

@dp.message_handler(text_contains="Qo'llanma")
async def select_category(msg: types.Message):
    text = f"Assalomu aleykum hurmatli foydalanuvchi. Siz bu yerda oliy ta'limdagi qiyinchiliklaringizga yechim topasiz. Quyidagi sohalar bo'yicha o'z muammolaringizga yechim toping:\n\n✅ Dasturlash (bir nechta sohalar)\n✅ Ingliz tili\n✅ Modellashtirish (MathCad)\n✅ Photoshop, CorellDraw, AutoCad\n✅ Hisoblash tizimlari, Oliy matematika.\n\n Shu bilan birgalikga buyruqlar menyusidan /registration orqli ro'yxatdan o'ting yoki xizmatlar bo'limidan kerakli bo'limni tanlashingiz orqali biz sizga aloqaga chiqamiz.\n\n🤝 Bir zumda uydan turib hal qiling."
    with open("assets/images/guide.jpg", "rb") as photo:
        await msg.answer_photo(photo=photo, caption=text)

@dp.callback_query_handler(text="courses")
async def request_service(call: types.CallbackQuery):
    await call.message.answer("Xizmat turini tanglang", reply_markup=serviceMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="books")
async def request_service(call: types.CallbackQuery):
    await call.answer("Kitoblar hali yuklanmadi. Xizmatlarimizdan foydalanganingiz uchun tashakkur !...", cache_time=60,show_alert=True)

@dp.callback_query_handler(course_callback.filter(item_name="dasturlash"))
async def request_service(call: types.CallbackQuery):
    await call.message.answer("Yo'nalishni tanglang", reply_markup=programmingMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(course_callback.filter(item_name="english"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: Ingliz tili)", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(course_callback.filter(item_name="model"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: Modellashtirish (MathCad).", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(course_callback.filter(item_name="graph"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: Photoshop, CorellDraw, AutoCad)", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(course_callback.filter(item_name="math"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: Hisoblash tizimlari, Oliy matematika)", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(programming_callback.filter(item_name="python"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: Python) Xizmatlar: Web, Data analyse, Data vizualation, Computer Vision.", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(programming_callback.filter(item_name="javascript"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: Javascript) Xizmatlar: Web, VueJs, NextJs, Js.", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(programming_callback.filter(item_name="frontend"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: 🌎 HTML, CSS, Bootstrap , Tailwind, Js, JQuery) Xizmatlar: Static web sahifalar yaratish", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(programming_callback.filter(item_name="mbbt"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: 🧩 MBBT) Xizmatlar:SQL, MySQL, PostgreSQl, Sqlite3, Access", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")

@dp.callback_query_handler(programming_callback.filter(item_name="php"))
async def request_english(call: types.CallbackQuery, callback_data: dict):
    course = callback_data.get("item_name")
    await call.answer("So'rovingiz qabul qilindi (Tanlov: 🧩 Php) Xizmatlar: web, XAMPP", cache_time=60,show_alert=True)
    user = call.from_user.id
    time = dt.now(tz=tz).strftime("%d-%B , %Y | %H:%M:%S")
    if call.from_user.username:
        user = call.from_user.username
    else:
        user=call.from_user.id
    await call.bot.send_message(chat_id=6292468270, text=f"{course} selected by @{user} at {time}.")


@dp.callback_query_handler(text="cancel")
async def request_service(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=serviceMenu)