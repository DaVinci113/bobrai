from aiogram.filters import CommandStart, Command
from aiogram import Router, types
from weather import get_data

user_router = Router()


@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('БОТ запущен!')


@user_router.message(Command('weather'))
async def echo(message: types.Message):
    user_id = message.from_user.id
    msg = message.text
    if message.text.startswith('/weather'):
        city = message.text[9::].strip()
        await message.answer(f'Выбран город {city}\nОжидайте...')
        await message.reply(get_data(city, user_id, msg))
