import asyncio
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
from config import TOKEN, NASA_API_KEY
import requests


bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_random_apod():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + (end_date - start_date) * random.random()
    date_str = random_date.strftime('%Y-%m-%d')
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={date_str}"
    response = requests.get(url)
    #response.raise_for_status()
    return response.json()


@dp.message(Command('apod'))
async def send_apod(message: Message):
    apod = get_random_apod()
    photo_url = apod['url']
    title = apod['title']
    description = apod['explanation']
    await message.answer_photo(photo_url, caption=f"{title}\n{description}\n")

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer("Привет! Используй команду /apod, чтобы получить случайное астрономическое фото.")


async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())