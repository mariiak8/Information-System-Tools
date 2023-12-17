import logging
from aiogram import Bot, Dispatcher, executor, types

import config as cfg

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

# получение id пользователя
#@dp.message_handler(commands=["test"], commands_prefix="/")
#async def test(message: types.Message):
#    await bot.send_message(message.from_user.id, f"Your ID: {message.from_user.id}")

# приветствие новых юзеров
@dp.message_handler(content_types=["new_chat_members"])
async def user_joined(message: types.Message):
    await message.answer("Добро пожаловать!")

# удаление сообщений по словарю
@dp.message_handler()
async def mess_handler(message: types.Message):
    text = message.text.lower()
    for word in cfg.WORDS:
        if word in text:
            await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
