from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


info_button = KeyboardButton("/start")


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

keyboard.add(info_button)
