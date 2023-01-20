# for this example you will need to copy the file
# logo_supsi.py onto the board's storage 
from machine import I2C
from time import sleep_ms

import sh1107
from logo_supsi import logo

invert = False

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 128
i2cbus = I2C(0)

oled = sh1107.SH1107_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2cbus)


oled.blit(logo, -1, 37)
oled.show()

while(True):
    oled.invert(invert)
    oled.show()
    invert = not invert
    sleep_ms(300)

