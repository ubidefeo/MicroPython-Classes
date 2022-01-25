# main.py -- put your code here!
from machine import Pin
import time

led = Pin(6, Pin.OUT)

def setup():
    print('ready!')

def loop():
    led.on()
    time.sleep_ms(150)
    led.off()
    time.sleep_ms(100)
    led.on()
    time.sleep_ms(150)
    led.off()
    time.sleep_ms(600)

def cleanup():
    # add code here that will execute at a keyboard interrupt
    # such as deinit() for Timer objects and so on
    pass