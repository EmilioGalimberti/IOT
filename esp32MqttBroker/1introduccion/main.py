#https://wokwi.com/projects/373687794234134529
# En este caso usaremos al esp32 como publicador para el topico
# import unique_id del esp32, este permite el indicador unico del esp32
from machine import Pin, Timer, unique_id
import dht
import time
import json
import ubinascii
from collections import OrderedDict
from settings import SERVIDOR_MQTT
# u hace referencia  a lo de mycropython
from umqtt.robust import MQTTClient

# Decodificamos el unqique_id pasandolo a una cadena
# luego lo utilizaremos para identificar que es el que publica al topic
CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

# Creamos el objeto del cliente, Si el broker tendria usario y contraseña se lo deberiamos agg como params
# keepalive=10 si despues de 10 segundos no hay ninguna interaccion se cancelara sola la suscripcion
mqtt = MQTTClient(CLIENT_ID, SERVIDOR_MQTT,
                  port=8883, keepalive=10, ssl=True)

led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
contador = 0


def heartbeat(nada):
    global contador
    if contador > 5:
        pulsos.deinit()
        contador = 0
        return
    led.value(not led.value())
    contador += 1


def transmitir(pin):
    print("publicando")
    mqtt.connect()
    # el primer argumento es el topico a cual se publica
    mqtt.publish(f"ap/{CLIENT_ID}", datos)
    # Desconecatmos para ahorra recursos, si nos conectamos a mas de 1 nos quedaremos sin memoria
    mqtt.disconnect()
    # incializacion de hearthbeat
    pulsos.init(period=150, mode=Timer.PERIODIC, callback=heartbeat)


# Interrupcion de tiempo, que ese ejecuta cada 30s
publicar = Timer(0)
publicar.init(period=30000, mode=Timer.PERIODIC, callback=transmitir)
# creacion de segundo timer pero no inicializado
pulsos = Timer(1)

while True:
    try:
        d.measure()
        temperatura = d.temperature()
        humedad = d.humidity()
        datos = json.dumps(OrderedDict([
            ('temperatura', temperatura),
            ('humedad', humedad)
        ]))
        print(datos)
    except OSError as e:
        print("sin sensor")
    time.sleep(5)
