from time import sleep
from machine import I2C, Pin
from i2c_lcd import Display


i2c_bus = I2C(id = 0)
display = Display(i2c_bus, lcd_addr = 0x3e2)

display.clear()
display.write('Hello,')
sleep(0.5)
display.move(0, 1)
sleep(0.5)
display.write('World!')

