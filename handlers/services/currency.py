import requests

from handlers.models.currency import CurrencyModel


class CurrencyService:

	def __init__(self, key):
		self.key = key

	def get_currency(self, currency_id):
		url = f'https://rest.coinapi.io/v1/assets?filter_asset_id={currency_id}'
		headers = {
			'X-CoinAPI-Key': self.key,
		}
		response = requests.get(url, headers=headers).json()
		if not response:
			return "Похоже, такой криптовалюты нет. Проверьте правильность написания id"
		coin = dict(CurrencyModel.parse_obj(response[0]))
		return f"You searched for <b>{coin['name']}</b>\n" \
			f"- Asset id: {coin['asset_id']}\n" \
			f"- Price in USD: {coin['price_usd']}\n\n" \
			f"Original Api: <b>/API</b>"
