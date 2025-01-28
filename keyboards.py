from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")]],
    resize_keyboard=True)

inline_links = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Новости", url="https://news.google.com/"),
        InlineKeyboardButton(text="Музыка", url="https://music.youtube.com/")
    ],
    [
        InlineKeyboardButton(text="Видео", url="https://youtube.com/")
    ]
])

dynamic = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Показать больше', callback_data='show_more')
    ]
])

new_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Опция 1", callback_data="option_1"),
        InlineKeyboardButton(text="Опция 2", callback_data="option_2")
    ]
])


async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()
