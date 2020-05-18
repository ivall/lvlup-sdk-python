import requests

url = "https://api.lvlup.pro/v4/"


class Payments(object):
    def __init__(self, api_key):
        self._api_key = api_key

    def create_payment(self, amount, redirectUrl="", webhookUrl=""):

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self._api_key,
            "Content-Type": "application/json",
        }
        data = '{ "amount": "%s", "redirectUrl": "%s", "webhookUrl": "%s"}' % (
            amount,
            redirectUrl,
            webhookUrl,
        )

        response = requests.post(url + "wallet/up", headers=headers, data=data)

        return response.json()

    def is_paied(self, id):

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self._api_key,
        }

        response = requests.get(url + "wallet/up" + id, headers=headers)

        info = response.json()

        if info["payed"]:
            return True
        return False

    def balance(self):
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self._api_key,
        }

        response = requests.get(url + "wallet", headers=headers)
        return response.json()

    def payments(self, limit):
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer " + self._api_key,
        }

        params = (("limit", str(limit)),)

        response = requests.get(url + "payments", headers=headers, params=params)
        return response.json()
