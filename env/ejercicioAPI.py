import requests

URL = 'https://randomuser.me/api/'

response=requests.get(URL, params = {'results': 10})#solo devuelva 10 usuarios

if response.status_code == 200:
   response = response.json()
   print(response)
   results = response.get('results')
   #print(results)

   for user in results:
       name = user.get('name')
       
       location = user.get('location')
       country = location['country']
       state = location['state']
       city = location['city']
       email = user.get('email')       

       print('###########################################')
       print(f"Name: {name['title']} {name['first']} {name['last']} ")
       print(f"Location: {location['street']['name']} {location['street']['number']}")
       print(f"Email: { email } ")
       print(f"Country: { country } ")
       print(f"State: { state } ")
       print(f"Ciudad: { city } ")
              
       print('###########################################')
       print('')
  
