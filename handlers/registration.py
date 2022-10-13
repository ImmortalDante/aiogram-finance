from aiogram import Dispatcher

from handlers.client.client import start


def register_client_handlers(dispatcher: Dispatcher):
	dispatcher.register_message_handler(start, commands=["start", "help", "hello"])
