#Dos interrupciones combinadas
#Heartbeat se utiliza como una señal de vida para saber que el dispositivo sigue activo
#https://wokwi.com/projects/373609335527681025
from machine import Pin, Timer

led = Pin(2, Pin.OUT)
contador=0

def latir(nada):
  global contador
  print(contador)
  if contador > 3:
    #Desactiva o desincializa esta funcion
    #Es decir desactiva esta interrupcion, Timer
    pulsos.deinit()
    contador=0
    return
  led.value(not led.value())
  contador +=1

def heartbeat(nada):
  pulsos.init(period=150, mode=Timer.PERIODIC, callback=latir)

periodo = Timer(0)
periodo.init(period=3000, mode=Timer.PERIODIC, callback=heartbeat)
pulsos = Timer(1)

# esto es independiente es decir que podria tener otras estructuras sin ningun problema