import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

# response = requests.get(url, params={'symbol': 'BTCUSDT'})
# next_json = response.json()
# print(next_json)


s = []
for i in range(10):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    s.append(price)
    time.sleep(1)


print(s)
print(max(s))
print(min(s))





