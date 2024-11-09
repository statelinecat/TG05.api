from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import  InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет!'), KeyboardButton(text='Пока!')]
], resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости', url='https://dzen.ru/news/')],
    [InlineKeyboardButton(text='Музыка', url='https://zaycev.net/')],
    [InlineKeyboardButton(text='Видео', url='https://vk.com/video')]
])

inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data= 'dynamic')],
])

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


