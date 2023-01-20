from machine import I2C, Pin
from ssd1306_1315 import SSD1306_I2C
from random import randint
from time import sleep_ms

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coords(coords):
        pass

old_coords = Point(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
new_coords = old_coords

# Arduino Nano RP2040 Connect I2C0 pins: 
# SDA: A4 (rp2 Pin 12)
# SCL: A5 (rp2 Pin 13)

# Arduino Nano RP2040 Connect I2C1 pins: 
# SDA: A0 (rp2 Pin 26)
# SCL: A1 (rp2 Pin 27)

i2cbus = I2C(1) 

oled = ssd1306.SSD1306_I2C(128, 64, i2cbus)
oled.fill(0)
oled.show()
oled.text('Arduino', 40, 40)
oled.text('vs', 60, 54)
oled.text('MicroPython', 23, 68)
oled.show()

def new_random_point():
    new_x = randint(0, DISPLAY_WIDTH)
    new_y = randint(0, DISPLAY_HEIGHT)
    new_coords.x = new_x
    new_coords.y = new_y
    oled.line(old_coords.x, old_coords.y, new_coords.x, new_coords.y, 1)
    oled.show()
    old_coords.x = new_x
    old_coords.y = new_y
    return

def new_random_offset():
    new_x_offset = randint(-5, 5)
    new_y_offset = randint(-5, 5)
    new_coords.x += new_x_offset
    new_coords.y += new_y_offset

    if(new_coords.x > DISPLAY_WIDTH):
        new_coords.x = DISPLAY_WIDTH
    if(new_coords.x < 0):
        new_coords.x = 0
    if(new_coords.y > DISPLAY_HEIGHT):
        new_coords.y = DISPLAY_HEIGHT
    if(new_coords.y < 0):
        new_coords.Y = 0

    oled.line(old_coords.x, old_coords.y, new_coords.x, new_coords.y, 1)
    oled.show()
    old_coords.x = new_coords.x
    old_coords.y = new_coords.y

def reset_all():
    oled.fill(0)
    oled.show()
    
while(1):
    new_random_offset()
    sleep_ms(10)
