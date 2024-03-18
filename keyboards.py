from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton("O'zbek adabiyoti🌐"), KeyboardButton("Category💬")],
[KeyboardButton('Aloqa📞'), KeyboardButton('Biz haqimizdaℹ️')]
],resize_keyboard=True)

menu_detail = ReplyKeyboardMarkup([
    [KeyboardButton("👤Abdulla Qodiriy"),KeyboardButton("👤Cho'lpon")],
     [KeyboardButton("👤Oybek"),KeyboardButton("👤G'afur G'ulom")],
     [KeyboardButton("👤Abdulla Qahhor"),KeyboardButton("👤Said Ahmad")],
     [KeyboardButton("👤O'tkir Hoshimov"),KeyboardButton("👤Pirimqul Qodirov")],
     [KeyboardButton("👤Asqad Muxtor"),KeyboardButton("👤Odil Yoqubov")],
     [KeyboardButton("👤Tog'ay Murod"),KeyboardButton("👤Tohir Malik")],
    [KeyboardButton("Back to Menu")]
],resize_keyboard=True)

category_detail = ReplyKeyboardMarkup([
    [KeyboardButton("Category - 1"),KeyboardButton("Category - 2")],
     [KeyboardButton("Category - 3"),KeyboardButton("Category - 4")],
    [KeyboardButton("Back to Menu")]
],resize_keyboard=True)


menu_1 = ReplyKeyboardMarkup([
    [KeyboardButton("Kitoblari 📚")],
    [KeyboardButton("Hayoti va Ijodi⛓")],
[KeyboardButton("Back to Menu")]
    ],resize_keyboard=True
)


