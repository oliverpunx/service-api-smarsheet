import requests

URL="https://httpbin.org/post"

data = {
    'username': 'Ambar',
    'password': 'asdfgh'
}

response=requests.post(URL, data = data)

if response.status_code == 200:
   respuesta = response.json()

   print(respuesta)

