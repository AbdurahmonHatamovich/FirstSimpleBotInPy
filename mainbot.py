import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from main import Database

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)

    check_query = f"""SELECT * FROM users WHERE chat_id = '{chat_id}'"""
    if len(Database.connect(check_query, "select")) >= 1:
        await message.reply(f"Hello @{username}")

    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username} {Database.connect(query, "insert")} database")
        await message.reply(f"Hello @{username}")


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler(commands=['data'])
async def select(message: types.Message):
    chat_id = message.chat.id
    query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
    data = Database.connect(query_select, "select")
    print(data)
    await message.reply(f"""
        Salom @{data[0][3]}

        First Name: {data[0][1]}
        Last Name: {data[0][2]}""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)