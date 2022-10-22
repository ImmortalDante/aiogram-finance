from aiogram import types

import config
from keyboards.client import keyboard, currency_keyboard, exchange_keyboard


async def start(message: types.message):
	await message.answer(
		"Hello! I'm cryptocurrency bot! Use this commands to find out information about exchanges:\n"
		"- <b>/Kraken</b>\n"
		"- <b>/BINANCE</b>\n"
		"Original Api: <b>/API</b>",
		reply_markup=keyboard,
		parse_mode="html",
	)


async def currency_menu(message: types.Message):
	await message.answer("Currency menu", reply_markup=currency_keyboard)


async def exchange_menu(message: types.Message):
	await message.answer("Exchange menu", reply_markup=exchange_keyboard)


async def get_api(message: types.Message):
	await message.answer(config.API_URL)
