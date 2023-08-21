import dht
import machine
import time

# Configurar el pin al que está conectado el sensor DHT22
dht_pin = machine.Pin(4)

# Crear una instancia del sensor DHT22
dht_sensor = dht.DHT22(dht_pin)

while True:
    try:
        # Realizar la lectura del sensor
        dht_sensor.measure()
        humidity = dht_sensor.humidity()
        temperature = dht_sensor.temperature()

        # Mostrar los resultados en la terminal
        print("Humedad: {}% - Temperatura: {}°C".format(humidity, temperature))
    except OSError as e:
        print("Error al leer el sensor DHT22:", e)

    # Esperar 20 segundos antes de la próxima lectura
    time.sleep(20)