import asyncio, os, random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
# from gtts import gTTS
from config import TOKEN

import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text='Это главное меню. Выберите:',
        reply_markup=kb.main
    )

@dp.message(F.text == 'Привет')
async def on_greet(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == 'Пока')
async def on_bye(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(
        text='Полезные ссылки:',
        reply_markup=kb.inline_links
    )

@dp.message(Command("dynamic"))
async def dynamic(message: Message):
    await message.answer('Нажмите кнопку, чтобы показать больше опций', reply_markup=kb.dynamic)

@dp.callback_query(F.data == 'show_more')
async def show_more(callback: CallbackQuery):
    await callback.message.edit_text(
        'Выберите опцию:',
        reply_markup=kb.new_kb
    )

@dp.callback_query(F.data.in_({'option_1', 'option_2'}))
async def option_selected(callback: CallbackQuery):
    option = callback.data
    if option == 'option_1':
        text = 'Вы выбрали Опцию 1'
    else:
        text = 'Вы выбрали Опцию 2'
    await callback.message.answer(text)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
