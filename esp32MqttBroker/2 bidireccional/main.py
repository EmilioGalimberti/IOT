# mqttBidereccional
#https://wokwi.com/projects/373691417148294145
from machine import Pin, Timer, unique_id
import dht
import time
import json
import ubinascii
from collections import OrderedDict
from settings import SERVIDOR_MQTT
from umqtt.robust import MQTTClient

CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

mqtt = MQTTClient(CLIENT_ID, SERVIDOR_MQTT,
                  port=8883, keepalive=40, ssl=True)

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))

#prendermos y apagaremos el led remotamente
def sub_cb(topic, msg):
    print((topic, msg))
    if msg==b"apagar":
        led.value(0)
    if msg==b"encender":
        led.value(1)

#defino que funcion invocar cuando recibo un mensaje
mqtt.set_callback(sub_cb)
#la conexion la realizamos fuera de toda funcion, ya que lo mantedremos conectado y funcionara como objeto global
mqtt.connect()
#nos suscribimos al topico
mqtt.subscribe(f"ap/{CLIENT_ID}/comando")

def transmitir(pin):
    mqtt.publish(f"ap/{CLIENT_ID}",datos)

#interrupcion por tiempo cada 20 segundos para publicar
timer1 = Timer(1)
timer1.init(period=20000, mode=Timer.PERIODIC, callback=transmitir)

datos={}

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
    #verificacion si hay mensaje nuevo, para el esp32
    #en el caso de que llegue se invoca la funcion definida por parametro en la fun callback
    mqtt.check_msg()
    time.sleep(5)

mqtt.disconnect()
