from aiogram import types

from keyboards.client import keyboard


async def start(message: types.message):
	await message.answer(
		"Hello!\n"
		"/Kraken\n"
		"/BINANCE\n"
		"/BTC\n",
		reply_markup=keyboard,
	)
