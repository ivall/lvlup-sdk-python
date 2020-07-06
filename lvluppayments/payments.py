import requests

class Payments(object):
    def __init__(self, api_key, config):
        if config == 'production':
          self.url = "https://api.lvlup.pro/v4/"
        elif config == 'sandbox':
          self.url = "https://sandbox-api.lvlup.pro/v4/"
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + api_key,
        }

    def create_payment(self, amount, redirect_url="", webhook_url=""):

        data = '{ "amount": "%s", "redirectUrl": "%s", "webhookUrl": "%s"}' % (amount,redirect_url,webhook_url,)

        response = requests.post(self.url + "wallet/up", headers=self.headers, data=data)

        return response.json()

    def is_paid(self, id):

        response = requests.get(self.url + "wallet/up" + id, headers=self.headers)

        info = response.json()

        return info["payed"]

    def balance(self):

        response = requests.get(self.url + "wallet", headers=self.headers)
        return response.json()

    def payments(self, limit):

        params = (("limit", str(limit)),)

        response = requests.get(self.url + "payments", headers=self.headers, params=params)
        return response.json()
