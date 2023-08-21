#Solamente

import urequests
#get   (solicitamos el contenido de la pagina)
response = urequests.get('https://www.smn.gob.ar/')
#buscamos lo que esta antes del token
inicio = response.content.decode('UTF-8').find("localStorage.setItem('token', ")
#buscamos el final del token, apartir del inicio del token
fin = response.content.decode('UTF-8').find("'",inicio+32)
#token
token = response.content.decode('UTF-8')[inicio+31:fin]
#encabezado con key Authorization + token
encabezado = {'Authorization': f'JWT {token}'}
#hagp la consulta get con la autorizacion
datos = urequests.get('https://ws1.smn.gob.ar/v1/weather/location/9743', headers=encabezado)
print(datos.json())
#mostramos solo la temperatura
temperatura = f"{datos.json()['temperature']}".replace('.', ',')
print(f"Temperatura {temperatura} C")

