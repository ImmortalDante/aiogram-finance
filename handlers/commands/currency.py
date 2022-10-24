from aiogram import types

import config
from handlers.services.currency import CurrencyService


service = CurrencyService(config.API_KEY)


async def get_currency(message: types.Message):
	await message.answer(
		service.get_currency(message.text),
		parse_mode="html"
	)
