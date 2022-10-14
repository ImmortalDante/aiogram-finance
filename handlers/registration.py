from aiogram import Dispatcher

from handlers.commands.client import start
from handlers.commands.currency import get_bitcoin
from handlers.commands.exchanges import get_kraken, get_binance


def register_client_handlers(dispatcher: Dispatcher):
	dispatcher.register_message_handler(start, commands=["start", "help", "hello"])
	dispatcher.register_message_handler(get_kraken, commands=["Kraken"])
	dispatcher.register_message_handler(get_binance, commands=["BINANCE"])
	dispatcher.register_message_handler(get_bitcoin, commands=["BTC"])
