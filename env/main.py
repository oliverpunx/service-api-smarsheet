import requests

URL="https://httpbin.org/get"

response = requests.get(URL)

print(response)#valore que devuelve la respuesta
print(response.status_code)# codigo http de la respuesta
print(response.text)#objeto que devuelve GET
print(response.json())#objeto que devuelve GET convertido a objeto JSON (dictionary)

request=response.json();
#obtengo un atributo del objeto respuesta
print(request.get('origin'));

#query
print("**************query API**************")
URL="https://httpbin.org/get?name=eduardo&password=123&email=eduardo@mail.com"

parametros ={
    'name': 'Miguel López',
    'password': 'punkhc',
    'email': 'miguel@yahoo.com'
}

#forma 1
response=requests.get(URL)
if response.status_code == 200:
   print(response)
   response=response.json()
   params=response['args']

   print (params['name'])
   print (params['password'])
   print (params['email'])

#forma 2
response=requests.get(URL,params = parametros)
if response.status_code == 200:
   print(response)
   response=response.json()
   params=response['args']

   print (params['name'])
   print (params['password'])
   print (params['email'])   