#https://wokwi.com/projects/370161344133188609
from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador = 0
while True:
    if sw.value():
        contador += 1
        print(contador)
        if contador == 3:
            print('Pulsacion larga')
    else:
        if contador == 2:
            print("Pulsacion corta")
        contador = 0
    time.sleep_ms(250)

    # El tiempo de de espera le permite reaccionar bien al prendido y apagado contra el pulsador