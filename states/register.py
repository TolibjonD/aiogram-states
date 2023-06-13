from aiogram.dispatcher.filters.state import StatesGroup , State

class RegistrationState(StatesGroup):
    fullName = State()
    email = State()
    phone = State()
    address = State()