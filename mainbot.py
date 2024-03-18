import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types,executor
from main import Database
from keyboards import menu_keyword, menu_detail, menu_1
from inline_keywords.post import inline_keyword_1
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
        print(f"{username}")
        await message.answer(f"Assalomu alekum @{username} botimizga hush kelibsiz😊\nMa'lumot izlamoqchi bo'lsangiz oddiygina bo'limlarda birini tanlashingiz mumkin☺️",reply_markup=menu_keyword)


    else:
        print(f"{first_name} start bot")
        query = f"""INSERT INTO users(first_name, last_name, username, chat_id) VALUES('{first_name}', '{last_name}', '{username}', '{chat_id}')"""
        print(f"{username} {Database.connect(query, "insert")} database")
        print(f"{username}")
        await message.answer(f"Hello @{username}",reply_markup=menu_keyword)




# @dp.message_handler(commands=['data'])
# async def select(message: types.Message):
#     chat_id = message.chat.id
#     query_select = f"SELECT * FROM users WHERE chat_id = '{chat_id}'"
#     data = Database.connect(query_select, "select")
#     print(data)
#     await message.reply(f"""
#         Salom @{data[0][3]}
#
#         First Name: {data[0][1]}
#         Last Name: {data[0][2]}""")




@dp.message_handler(lambda message: message.text == "O'zbek adabiyoti🌐")
async def show_menu(message: types.Message):
    await message.answer("Mualifflardan birini tanlang ",reply_markup=menu_detail)

@dp.message_handler(lambda message: message.text == "Category💬")
async def show_category(message: types.Message):
    await message.answer("Categorilardan birini tanlang ",reply_markup=inline_keyword_1)

@dp.message_handler(commands=['Aloqa📞'])
async def show_contact(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Taklif va shikoyatlar uchun @hwryubro 🔚 shu adminga murojaat qilishingiz mumkin")

@dp.message_handler(commands=['Biz haqimizdaℹ️'])
async def show_about(message: types.Message):
    await message.answer("TELEFON: +998 90 917 78 50\nE-MAIL: muruvat@gmail.com\nISH VAQTI: du-yak 24/7\nMANZIL: 100187, Tоshkent shahar, Shayxontohur tumani, Navoiy ko'chasi, 2a")



@dp.message_handler(lambda message: message.text == "Back to Menu")
async def back(message: types.Message):
    await message.answer("Menu yoki Categoriyani tanlang ",reply_markup=menu_keyword)

@dp.message_handler(lambda message: message.text == "👤Abdulla Qodiriy")
async def menu_01(message: types.Message):
# action = button_callback_menu.new(action=message.text)
    await message.answer ("👤Abdulla Qodiriy", reply_markup=menu_1)


#admin
@dp.message_handler(commands=['data'])
async def admin_command(message: types.Message):
    if message.from_user.id in [6576395985]:
        await message.reply("Salom admin")
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


@dp.callback_query_handler(lambda call: call.data == 'Ozbekadabiyoti')
async def agree_ref_start(query: types.CallbackQuery):
    if query.data == 'Ozbekadabiyoti':
        await query.answer("Ozbek adabiyoti ustiga bostingiz!")

@dp.callback_query_handler(lambda call: call.data == 'Mumtozadabiyoti')
async def agree_ref_start(query: types.CallbackQuery):
    if query.data == 'Mumtozadabiyoti':
        await query.answer("Mumtoz adabiyoti ustiga bostingiz!")

@dp.callback_query_handler(lambda call: call.data == 'Islomiykitoblar')
async def agree_ref_start(query: types.CallbackQuery):
    if query.data == 'Islomiykitoblar':
        await query.answer("Islomiy kitoblar ustiga bostingiz!")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)