from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import  InlineKeyboardBuilder

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
async def horo_kb():
    keyboard = InlineKeyboardBuilder()
    for zodiac_ru, zodiac_en in zodiac_signs:
        keyboard.add(InlineKeyboardButton(text=zodiac_ru, callback_data=zodiac_en))
        keyboard.adjust(2)
    return keyboard.as_markup()


