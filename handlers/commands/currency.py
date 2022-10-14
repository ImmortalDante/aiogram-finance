from aiogram import types
import requests

import config


async def get_bitcoin(message: types.message):
	url = 'https://rest.coinapi.io/v1/assets?filter_asset_id=BTC'
	headers = {
		'X-CoinAPI-Key': config.API_KEY,
	}
	response = requests.get(url, headers=headers).json()
	await message.answer(response)
