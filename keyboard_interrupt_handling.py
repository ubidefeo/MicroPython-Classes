# main.py -- put your code here!
from machine import Timer
import sys
from machine import Pin
import time
led = Pin(6, Pin.OUT)

ticker = Timer(-1)

def ticker_action(timer):
    print('tick')

ticker.init(mode = Timer.PERIODIC, period = 500, callback = ticker_action)
while(True):
    try:
        led.on()
        time.sleep_ms(150)
        led.off()
        time.sleep_ms(100)
        led.on()
        time.sleep_ms(150)
        led.off()
        time.sleep_ms(600)
    except KeyboardInterrupt:
        print('program stopped')
        ticker.deinit()
        sys.exit(0)
