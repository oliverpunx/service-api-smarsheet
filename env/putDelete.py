import requests

URL = 'https://httpbin.org/put'

response = requests.put(URL, params = {'name': 'Juan'}, headers = {'version': '2.0'}, data = {'id': 123})

if response.status_code == 200:
   print(response.text)

URL = 'https://httpbin.org/delete'

response = requests.delete(URL, params = {'name': 'Juan'}, headers = {'version': '2.0'}, data = {'id': 123})

if response.status_code == 200:
   print(response.text)   