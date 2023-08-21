#Utilizamos libreria para solucinar el rebote del pulsador
#https://wokwi.com/projects/373609520580382721
from machine import Pin
from debounce import DebouncedSwitch

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
total=0

def sumador(algo):
    global total
    total+=1
    print(total)
    led.value(not led.value())
    print(algo)

contador=DebouncedSwitch(sw, sumador)
