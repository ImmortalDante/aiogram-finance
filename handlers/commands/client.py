from aiogram import types


async def start(message: types.message):
	await message.answer(
		"Hello!\n"
		"/Kraken\n"
		"/BINANCE\n"
		"/BTC\n"
	)
