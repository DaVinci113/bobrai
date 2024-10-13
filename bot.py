import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
from hadlers.user import user_router


ALLOWED_UPDATES = ['message', 'edited_message']

load_dotenv(find_dotenv())

weather_token = os.getenv('WEATHER_TOKEN')

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())
