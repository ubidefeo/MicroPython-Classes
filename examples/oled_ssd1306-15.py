from machine import SoftI2C, Pin
import ssd1306_1315 as ssd1306
import gc
from random import randint
from time import sleep_ms
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_coords(coords):
        return
old_coords = Point(64, 32)
new_coords = Point(64, 32)
# old_coords = ["x": 0, "y":0]
# new_coords = ["x": 0, "y": 0]
i2cbus = SoftI2C(scl = Pin(13), sda = Pin(12), freq = 100000)
print(i2cbus)
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2cbus)
# oled.fill(0)
oled.show()
oled.text('Arduino', 40, 12)
oled.text('vs', 60, 26)
oled.text('MicroPython', 23, 45)
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
    gc.collect()
    oled.fill(0)
    oled.show()
        
    
while(1):
    new_random_offset()
    sleep_ms(10)