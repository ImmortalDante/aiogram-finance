from aiogram import types

from keyboards.client import keyboard, currency_keyboard, exchange_keyboard


async def start(message: types.message):
	await message.answer(
		"Hello!\n"
		"/Kraken\n"
		"/BINANCE\n"
		"/BTC\n",
		reply_markup=keyboard,
	)


async def currency_menu(message: types.Message):
	await message.answer("Currency menu", reply_markup=currency_keyboard)


async def exchange_menu(message: types.Message):
	await message.answer("Exchange menu", reply_markup=exchange_keyboard)
