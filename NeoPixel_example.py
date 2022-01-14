import machine, neopixel
from time import sleep
# PIXEL_PIN   = machine.Pin(21, machine.Pin.OUT)
PIXEL_NUMBER = 24
np = neopixel.NeoPixel(machine.Pin(21), PIXEL_NUMBER)
purple = (200, 0, 200)
black = (0, 0, 0)
np.fill(black)
np.write()
def ringUp():
    for i in range(0, PIXEL_NUMBER):
        np[i] = purple
        np.write()
        sleep(0.1)
        
def ringDown():
    for i in range(0, PIXEL_NUMBER):
        np[i] = black
        np.write()
        sleep(0.1)
        
def ringOff():
    for i in range(0, PIXEL_NUMBER):
        np[i] = black
    np.write()
    
def runPixelRun():
    while(1):
        ringUp()
        ringDown()
    
runPixelRun()
