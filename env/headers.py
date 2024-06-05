import requests

URL = "https://httpbin.org/post"

#cualquier metodo (get, post, put, delete) puede enviar info en el encabezado
headers = {
    'course': 'Curso de Python',
    'version': '2.0',
    'author': 'Eduardo Ismael'
} 

params = {
    'platform': 'Codigo Facilito'
}

data = {
    'username': 'mrlopes',
    'password': '123456'
}

response = requests.post(URL, headers = headers,params = params, data = data)

if response.status_code == 200:
   print(response.text)