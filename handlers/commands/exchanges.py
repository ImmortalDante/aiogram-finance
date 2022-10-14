from aiogram import types

import config
from handlers.services.exchanges import ExchangesService


service = ExchangesService(config.API_KEY)


async def get_kraken(message: types.message):
	await message.answer(service.get_exchange("Kraken"))


async def get_binance(message: types.message):
	await message.answer(service.get_exchange("BINANCE"))
