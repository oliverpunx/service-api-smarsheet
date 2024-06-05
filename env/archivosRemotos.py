import requests

URL = 'https://codigofacilito.com/images/'

response = requests.get(URL, stream = True)#le indica al servidor que se va a realizar una descarga
#y que mantenga la conexion durante la descarga

print(response.status_code)

#if response.status_code == 200:
print(response.text)

try:
        with open('images/cody.png','wb') as file:
             #va descargando por partes el archivo
             try:
                for chunk in response.iter_content(1024):
                    try:
                        file.write(chunk)
                    
                    except Exception as err:
                           print("Error file-write: "+err) 
            
             except Exception as err:
                    print("Error for-chunk: "+err) 

        print('Descarga exitosa')

except Exception as err:
       print("Error with-open: "+err) 
#else:
 #  print("No se pudo conectar a la API: ")
