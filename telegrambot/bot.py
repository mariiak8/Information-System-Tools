import logging
from aiogram import Bot, Dispatcher, executor, types

from asyncio import sleep

import config as cfg

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

# игра в кости в лс
@dp.message_handler(commands=['game'])
async def on_message(message: types.Message):
    await bot.send_message(message.from_user.id, f"О, {message.from_user.username}! Сейчас сыграем в личных сообщениях!")
    await sleep(1)

    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)

    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, "Вы проиграли боту!")
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, "Вы обыграли бота!")
    else:
        await bot.send_message(message.from_user.id, "Ничья.")


# получение id пользователя
# @dp.message_handler(commands=["test"], commands_prefix="/")
# async def test(message: types.Message):
#    await bot.send_message(message.from_user.id, f"Your ID: {message.from_user.id}")

# приветствие новых юзеров
@dp.message_handler(content_types=["new_chat_members"])
async def user_joined(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.username}!")


# удаление сообщений по словарю
@dp.message_handler()
async def mess_handler(message: types.Message):
    text = message.text.lower()
    for word in cfg.WORDS:
        if word in text:
            await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
