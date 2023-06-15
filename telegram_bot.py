from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = "TOKEN"
WEB_PAGE = "DOMAINE NAME"

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    button = InlineKeyboardMarkup()
    button.add(InlineKeyboardButton("Open", web_app=WebAppInfo(url=WEB_PAGE)))

    await message.answer("Hello!", reply_markup=button)

@dp.message_handler(commands=["photo"])
async def photo(message: types.Message):
    button = InlineKeyboardMarkup()
    button.add(InlineKeyboardButton("Open", web_app=WebAppInfo(url=f"{WEB_PAGE}photos")))

    await message.answer("There is your photos!", reply_markup=button)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
