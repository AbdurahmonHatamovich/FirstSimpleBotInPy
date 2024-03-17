from aiogram import types

inline_keyword_1 = types.InlineKeyboardMarkup(row_width=3)
button_1 = types.InlineKeyboardButton(text="Ozbek adabiyoti", callback_data="Ozbekadabiyoti")
button_2 = types.InlineKeyboardButton(text="Jahon adabiyoti", callback_data="Jahonadabiyoti")
button_3 = types.InlineKeyboardButton(text="Mumtoz adabiyoti", callback_data="Mumtozadabiyoti")
button_4 = types.InlineKeyboardButton(text="Islomiy kitoblar", callback_data="Islomiykitoblar")
inline_keyword_1.add(button_1, button_2)
inline_keyword_1.add(button_3,button_4)