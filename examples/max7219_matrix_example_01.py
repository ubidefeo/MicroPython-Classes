from machine import Pin

from time import sleep
from machine import SPI
from max7219 import Matrix8x8


spi = SPI(0)
cs = Pin(18)

display = Matrix8x8(spi, cs, 1)

display.fill(0)

display.show()

row = 0
col = 0
        
def advancePixel():
    global col, row
    col = col + 1
    if col >= 8:
        col = 0
        row = row + 1
        if row >=8:
            row = 0

while(1):
    sleep(0.1)
    if row == 0 and col == 0:
        display.fill(0)
        display.show()
    display.pixel(col, row, 1)
    display.show()
    advancePixel()
    