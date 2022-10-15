from aiogram import types

import config
from handlers.services.currency import CurrencyService


service = CurrencyService(config.API_KEY)


async def get_bitcoin(message: types.Message):
	await message.answer(service.get_currency("BTC"))


async def get_ethereum(message: types.Message):
	await message.answer(service.get_currency("ETH"))


async def get_doge(message: types.Message):
	await message.answer(service.get_currency("DOGE"))


async def get_u_coin(message: types.Message):
	await message.answer(service.get_currency("U"))


async def get_currency(message: types.Message):
	await message.answer(service.get_currency(message.text))
