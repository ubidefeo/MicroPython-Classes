from machine import Pin
from time import sleep

led = Pin(6, Pin.OUT)

while(True):
    led.on()
    sleep(1)
    led.off()
    sleep(1)

# the same effect can be created using the .toggle() command of the Digital Pin
# to try, replace the above "while" block with what's included in the triple quote, 
# making sure not to have unwanted spaces in the code
'''

while(True):
    led.toggle()
    sleep(1)

'''
