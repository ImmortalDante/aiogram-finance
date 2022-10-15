import requests


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
		return response
