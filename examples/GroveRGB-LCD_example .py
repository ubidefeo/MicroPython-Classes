from time import sleep
from machine import I2C, Pin
from i2c_lcd import RGBDisplay


i2c_bus = I2C(id = 0)
display = RGBDisplay(i2c_bus, lcd_addr = 0x3e, rgb_addr, 0x62)

display.clear()
display.write('Hello,')
sleep(0.5)
display.move(0, 1)
sleep(0.5)
display.write('World!')

while t in range(0,3):
  display.color(200, 0, 200)
  sleep(0.5)
  display.color(0, 0, 0)
  sleep(0.5)
