from aiogram import Dispatcher

from handlers.client.client import start, get_exchange, get_currency


def register_client_handlers(dispatcher: Dispatcher):
	dispatcher.register_message_handler(start, commands=["start", "help", "hello"])
	dispatcher.register_message_handler(get_exchange, commands=["Kraken"])
	dispatcher.register_message_handler(get_currency, commands=["BTC"])
