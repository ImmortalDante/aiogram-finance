import requests


class ExchangesService:
	def __init__(self, key):
		self.key = key

	def get_exchange(self, exchange_id):
		url = f"https://rest.coinapi.io/v1/exchanges?filter_exchange_id={exchange_id}"
		headers = {
			"X-CoinAPI-Key": self.key,
		}
		response = requests.get(url, headers=headers).json()[0]["website"]
		return response
