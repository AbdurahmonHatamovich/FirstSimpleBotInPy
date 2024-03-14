from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


menu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton("Menu"), KeyboardButton("Category")],
[KeyboardButton("Malumot qidirish"), KeyboardButton("Biz haqimizda")]
],resize_keyboard=True)


menu_detail = ReplyKeyboardMarkup([
    [KeyboardButton("Menu 1"),KeyboardButton("Menu 2")],
     [KeyboardButton("Menu 3"),KeyboardButton("Menu 4")],
    [KeyboardButton("Back to Menu")]
],resize_keyboard=True)


category_detail = ReplyKeyboardMarkup([
    [KeyboardButton("Category - 1"),KeyboardButton("Category - 2")],
     [KeyboardButton("Category - 3"),KeyboardButton("Category - 4")],
    [KeyboardButton("Back to Menu")]
],resize_keyboard=True)


menu_1 = ReplyKeyboardMarkup([
    [KeyboardButton("1")],
    [KeyboardButton("2")],
[KeyboardButton("Back to Menu")]
    ],resize_keyboard=True
)


