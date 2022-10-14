from aiogram import types
import requests

import config


async def start(message: types.message):
	await message.answer("Hello!\n/Kraken\n/BTC")


async def get_exchange(message: types.message):
	url = 'https://rest.coinapi.io/v1/exchanges?filter_exchange_id=Kraken'
	headers = {
		"X-CoinAPI-Key": config.API_KEY,
	}
	response = requests.get(url, headers=headers).json()
	await message.answer(response[0]["website"])


async def get_currency(message: types.message):
	url = 'https://rest.coinapi.io/v1/assets?filter_asset_id=BTC'
	headers = {
		'X-CoinAPI-Key': config.API_KEY,
	}
	response = requests.get(url, headers=headers).json()
	await message.answer(response)
