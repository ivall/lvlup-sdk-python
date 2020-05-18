import requests

url = "https://api.lvlup.pro/v4/"

class Payments(object):
    def __init__(self, api_key):
        self._api_key = api_key
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self._api_key,
        }

    def create_payment(self, amount, redirect_url="", webhook_url=""):

        data = '{ "amount": "%s", "redirectUrl": "%s", "webhookUrl": "%s"}' % (amount,redirect_url,webhook_url,)

        response = requests.post(url + "wallet/up", headers=self.headers, data=data)

        return response.json()

    def is_paid(self, id):

        response = requests.get(url + "wallet/up" + id, headers=self.headers)

        info = response.json()

        if info["payed"]:
            return True
        return False

    def balance(self):

        response = requests.get(url + "wallet", headers=self.headers)
        return response.json()

    def payments(self, limit):

        params = (("limit", str(limit)),)

        response = requests.get(url + "payments", headers=self.headers, params=params)
        return response.json()
