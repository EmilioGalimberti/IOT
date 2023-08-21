#https://wokwi.com/projects/373625759319274497
#consulta a la api desde web
#https://api.telegram.org/bot{tokenDeMiBot}/sendMessage?chat_id={miId}&text=hola


from machine import Pin, Timer
import dht
import time
import json
from collections import OrderedDict
import urequests
#importamos del settings la informacion sensible
from settings import TOKEN, CHATID

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))

print("esperando pulsador")
contador=0
estado=False

def alternar(pin):
    global contador, estado
    if sw.value():
        if not estado:
            contador+=1
            print(contador)
            led.value(not led.value())
            try:
                data = {'chat_id': CHATID, 'text': datos}
                #urequests hace consultas a la web
                response = urequests.post("https://api.telegram.org/bot" + TOKEN + '/sendMessage', json=data)
                #Para ver el estado de la consulta
                print(response.text)
                #se cierra la consulta para ahorrar recursos
                response.close()
                print("envio correcto a telegram")
            except:
                print("fallo en el envio a telegram")
            estado = True
        else:
            estado = False

timer1 = Timer(1)
timer1.init(period=50, mode=Timer.PERIODIC, callback=alternar)

while True:
    try:
        d.measure()
        temperatura=d.temperature()
        humedad=d.humidity()
        datos=json.dumps(OrderedDict([
            ('temperatura',temperatura),
            ('humedad',humedad)
        ]))
        print(datos)
    except OSError as e:
        print("sin sensor")
    time.sleep(5)