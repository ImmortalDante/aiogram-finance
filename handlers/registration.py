from aiogram import Dispatcher

from handlers.commands.client import start, currency_menu, exchange_menu, get_api
from handlers.commands.currency import get_currency
from handlers.commands.exchanges import get_kraken, get_binance


def register_client_handlers(dispatcher: Dispatcher):
	dispatcher.register_message_handler(start, commands=["start", "help", "hello"])
	dispatcher.register_message_handler(currency_menu, commands=["Currency"])
	dispatcher.register_message_handler(exchange_menu, commands=["Exchange"])
	dispatcher.register_message_handler(get_kraken, commands=["Kraken"])
	dispatcher.register_message_handler(get_binance, commands=["BINANCE"])
	dispatcher.register_message_handler(get_api, commands=["API"])
	dispatcher.register_message_handler(get_currency)
