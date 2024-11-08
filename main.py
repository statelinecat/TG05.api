import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.formatting import Text

import logging
from aiogram.filters.callback_data import CallbackData

from keyboard import horo_kb


import random
import requests
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

zodiacs_en = {
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
    "aquarius",
    "pisces"
}

# @dp.register_callback_query_handler(Text(equals=zodiacs_en))
# async def news(callback: types.CallbackQuery):
#     await callback.answer("Гороскоп подгружается", show_alert=True)
#     await callback.message.answer('Вот гороскоп на сегодня!')

# @dp.callback_query(F.data in zodiacs_en)
# async def news(callback: CallbackQuery):
#    await callback.answer("Гороскоп подгружается", show_alert=True)
#    await callback.message.answer('Вот гороскоп на сегодня!')

@dp.callback_query(F.data.in_(zodiacs_en))
async def news(callback: CallbackQuery):
    await callback.answer("Гороскоп подгружается", show_alert=False)
    await callback.message.answer('Вот гороскоп на сегодня!')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("По команде /start сообщаю гороскоп на сегодня.")

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Выберите знак зодиака:", reply_markup=await horo_kb())

async def main():
    # Запуск поллинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())