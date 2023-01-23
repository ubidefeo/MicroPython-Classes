from machine import I2C, Pin
import sh1107
from time import sleep

i2cbus = I2C(0)

oled = sh1107.SH1107_I2C(128, 128, i2cbus)
oled.poweron()

oled.text('    Arduino!', 0, 0, 1)
oled.text('     loves', 0, 12, 1)
oled.text('  MicroPython', 0, 24, 1)
oled.show()

while(1):
    oled.poweroff()
    # oled.show()
    sleep(1)
    oled.poweron()
    # oled.show()
    sleep(1)