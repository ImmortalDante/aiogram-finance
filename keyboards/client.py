from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


info_button = KeyboardButton("/start")
exchange_button = KeyboardButton("/Exchange")
currency_button = KeyboardButton("/Currency")

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(info_button).row(exchange_button, currency_button)


bitcoin_button = KeyboardButton("BTC")
ethereum_button = KeyboardButton("ETH")
doge_button = KeyboardButton("DOGE")
u_coin_button = KeyboardButton("U")

currency_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
currency_keyboard.row(bitcoin_button, ethereum_button).row(doge_button, u_coin_button)


binance_button = KeyboardButton("/BINANCE")
kraken_button = KeyboardButton("/Kraken")

exchange_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
exchange_keyboard.row(binance_button, kraken_button)
