# main.py -- put your code here!
from machine import Pin
import time

led = Pin(6, Pin.OUT)

while(True):
    led.on()
    time.sleep_ms(150)
    led.off()
    time.sleep_ms(100)
    led.on()
    time.sleep_ms(150)
    led.off()
    time.sleep_ms(600)
