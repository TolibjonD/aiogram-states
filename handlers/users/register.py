from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.default.register import btn

from states.register import RegistrationState
from loader import dp

import datetime as dt
import jinja2 
import pdfkit

@dp.message_handler(Command("registration"))
async def start_register(msg: types.Message):
    await msg.answer("Ro'yxatdan o'tish uchun quyidagilarni to'g'ri to'ldiring")
    await msg.answer("To'liq ismingizni yuboring (Namuna: Saidkodirov Tolibjon):")
    await RegistrationState.fullName.set()


@dp.message_handler(state=RegistrationState.fullName)
async def get_fullname(msg: types.Message , state=FSMContext):
    fullname = msg.text
    await state.update_data({
        "fullname":fullname
    })
    await msg.answer("Emailingizni yuboring (Namuna: admin@tolibjonD.com): ")
    await RegistrationState.next()

@dp.message_handler(state=RegistrationState.email)
async def get_email(msg: types.Message, state=FSMContext):
    email = msg.text
    await state.update_data({
        "email":email
    })
    await msg.answer("Telefon raqamingizni yuboring", reply_markup=btn)
    await RegistrationState.next()

@dp.message_handler(state=RegistrationState.phone, content_types=["contact"])
async def get_phone(msg: types.Message, state=FSMContext):
    phone = msg.contact.phone_number
    await state.update_data({
        "phone":phone
    })
    await msg.answer("Yashash manzilingizni kiriting (Namuna: Namnamgan vil, Pop t, Vodiy MFY ): ")
    await RegistrationState.next()

@dp.message_handler(state=RegistrationState.address)
async def get_address(msg: types.Message, state=FSMContext):
    address = msg.text
    await state.update_data({
        "address":address
    })
    data = await state.get_data()
    fullName = data.get("fullname")
    email = data.get("email")
    phone  = data.get("phone")
    address = data.get("address")

    time = dt.datetime.now().strftime("%d-%B , %Y | %H:%M:%S")
    context = {
        "time":time,
        "fullname":fullName,
        "email":email,
        "phone":phone,
        "address":address
    }

    temp_loader = jinja2.FileSystemLoader("./")
    temp_env = jinja2.Environment(loader=temp_loader)
    template = temp_env.get_template("template.html")
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
    pdfkit.from_string(output_text, f"{fullName}.pdf", configuration=config)

    full_data = "Quyidagi ma'lumotlar saqlandi:\n"
    full_data += f"Ismingiz: {fullName}\n"
    full_data += f"Email: {email}\n"
    full_data += f"Telefon: {phone}\n"
    full_data += f"Manzil: {address}"
    with open(f"{fullName}.pdf", "rb") as file:
        await msg.bot.send_document(chat_id=6292468270, document=file, caption="New user registered")
    await msg.answer(full_data)
    await state.reset_state()