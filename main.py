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
from googletrans import Translator

bot = Bot(token=TOKEN)
dp = Dispatcher()
horo_url = "https://ohmanda.com/api/horoscope/"
translator = Translator()


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


@dp.callback_query(F.data.in_(zodiacs_en))
async def news(callback: CallbackQuery):
    await callback.answer("Гороскоп подгружается", show_alert=False)
    zodiac = callback.data
    url = f"{horo_url}{zodiac}"
    response = requests.get(url, verify=False)
    data = response.json()
    translation = translator.translate(data['horoscope'], dest='ru')
    translated_text = translation.text
    await callback.message.answer(f'Вот гороскоп на сегодня:\n'
                                   f'{translated_text}')

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