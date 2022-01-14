from machine import SoftI2C, Pin
import sh1107
from time import sleep

i2cbus = SoftI2C(sda = Pin(29), scl = Pin(28))

oled = sh1107.SH1107_I2C(128, 128, i2cbus)

oled.poweron()

oled.text('- Hi, Arduino!', 0, 0, 1)
oled.text('- MicroPython!!!', 0, 12, 1)
oled.show()

while(1):
    oled.poweroff()
    # oled.show()
    sleep(1)
    oled.poweron()
    # oled.show()
    sleep(1)