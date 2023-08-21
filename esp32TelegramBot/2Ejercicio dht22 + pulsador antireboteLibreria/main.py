#https://wokwi.com/projects/373626270814658561
from machine import Pin
import dht
import time
import json
from collections import OrderedDict
import urequests
from debounce import DebouncedSwitch
from settings import TOKEN, CHATID

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))

print("esperand pulsador")
contador=0
estado=False

#Lo mismo que el anterior pero usando libreria antiRebote
#y nos evitamos usar el timer

def alternar(nada):
    global contador
    contador+=1
    print(contador)
    led.value(not led.value())
    try:
        data = {'chat_id': CHATID, 'text': datos}
        response = urequests.post("https://api.telegram.org/bot" + TOKEN + '/sendMessage', json=data)
        response.close()
        print("envio correcto a telegram")
    except:
        print("fallo en el envio a telegram")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

objeto=DebouncedSwitch(sw, alternar)

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