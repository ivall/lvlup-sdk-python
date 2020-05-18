import requests

def setApiKey(key):
  global apiKey
  apiKey = key

def createPayment(amount, redirectUrl="", webhookUrl=""):

  headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer '+apiKey,
      'Content-Type': 'application/json',
  }
  data = '{ "amount": "%s", "redirectUrl": "%s", "webhookUrl": "%s"}' % (amount,redirectUrl,webhookUrl,)

  response = requests.post('https://api.lvlup.pro/v4/wallet/up', headers=headers, data=data)

  try:
    return response.json()
  except Exception as e:
    return e

def checkPayment(id):

  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+apiKey,
  }

  response = requests.get('https://api.lvlup.pro/v4/wallet/up/'+id, headers=headers)

  info = response.json()
  if info['payed']:
    return True
  return False

def balance():
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+apiKey,
  }

  response = requests.get('https://api.lvlup.pro/v4/wallet', headers=headers)
  return response.json()

def paymentsList(limit):
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+apiKey,
  }

  params = (
      ('limit', str(limit)),
  )

  response = requests.get('https://api.lvlup.pro/v4/payments', headers=headers, params=params)
  return response.json()
