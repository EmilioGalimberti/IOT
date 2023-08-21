#https://wokwi.com/projects/370160966712923137
from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador=0
while True:
    if sw.value():
        led.value(not led.value())
        contador += 1
        print(contador)
        time.sleep_ms(250)
    #El tiempo de de espera le permite reaccionar bien al prendido y apagado contra el pulsador