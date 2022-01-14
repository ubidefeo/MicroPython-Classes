import dht
from machine import Pin
from time import sleep_ms

SENSOR_PIN = 5

snsr = dht.DHT11(Pin(SENSOR_PIN))
sleep_ms(500)

while(1):
    snsr.measure()
    print(snsr.temperature())
    print(snsr.humidity())
    sleep_ms(1000)