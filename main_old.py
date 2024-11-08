import asyncio
from aiogram import Bot, Dispatcher, F, types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

import random
import requests
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()

zodiac_signs = [
    ("Овен", "aries"),
    ("Телец", "taurus"),
    ("Близнецы", "gemini"),
    ("Рак", "cancer"),
    ("Лев", "leo"),
    ("Дева", "virgo"),
    ("Весы", "libra"),
    ("Скорпион", "scorpio"),
    ("Стрелец", "sagittarius"),
    ("Козерог", "capricorn"),
    ("Водолей", "aquarius"),
    ("Рыбы", "pisces")
]


@dp.message(Command('help'))
async def help(message: Message):
   await message.answer("По команде /start сообщаю гороскоп на сегодня.")

@dp.message(CommandStart())
async def send_welcome(message: Message):
    keyboard = InlineKeyboardMarkup()
    for sign, data in zodiac_signs:
            keyboard.add(InlineKeyboardButton(text=sign, callback_data=data))
    await message.answer("Выберите знак зодиака:", reply_markup=keyboard)



# async def main():
#    await dp.start_polling(bot)

async def main():
    # Подключение обработчиков
    # dp.include_router()
    # Запуск поллинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
   asyncio.run(main())