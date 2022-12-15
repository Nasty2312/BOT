import asyncio
from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)

#Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    text = f"Асаламалекум🫡, {message.from_user.full_name}, " \
      f"факт: работа программиста и шамана имеет много общего - оба бормочут непонятные слова, совершают непонятные действия и не могут объяснить, как оно работает."
    await message.answer(text=text)