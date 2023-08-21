#En este caso tenemos problemas para ejecutar mas de una tarea en un ciclo
#La solucion que tenemos a esto son las interrupciones por Timer
#Es decir interrupciones pausar la ejecucion del programa para ir atender otra porcion de codigo
#https://wokwi.com/projects/373607931267328001


from machine import Pin, Timer
import dht
import time
import json
from collections import OrderedDict

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
d = dht.DHT22(Pin(25))
print("esperand pulsador")
contador=0
estado=False

#Funcion para alternar el estado del led y incrementar contador
#En este caso se mejora el tema de la entre del pulsador y uso del led
def alternar(pin):
    global contador, estado
    #estado lo utilizamos para evitar el efecto rebote del pulsador y tome de a una pulsacion
    #el primer if valida si esta pulsado
    if sw.value():
        #este segundo if nos permite seguir  que no se siga sumando al contador
        #ya que si detecta que esta pulsado, el estado pasa a true y el no entrara en el segundo if
        if not estado:
            contador+=1
            print(contador)
            led.value(not led.value())
        estado = True
    else:
        estado = False


#Funcion timer
#El esp32 tiene varios timer en este caso usamos el 1
#Los timer son interrupcione por tiempo
#creamos el objeto
timer1 = Timer(1)
#Incializamos la interrupcion por timer
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
