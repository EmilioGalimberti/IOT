#Lo que esta dentro de este archivo se ejecutia por unica vez
#Cuando se inicia el esp32 y luego se pasa el control al main

#Extraigo la informacion sensible como id y pass del archivo settings
from settings import SSID, PASS_WLAN

#Codigo de ejemplo de micropyhon para conexion web

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASS_WLAN)
        #Este while se ejecuta indefinidamente hasta que se conecta a internet
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()