from machine import Pin
from machine import I2C



from time import sleep
from max7219 import Matrix8x8
from machine import SPI, SoftSPI

cs = Pin(18)
sck = Pin(20)
copi = Pin(19)
cipo = Pin(17)

spi = SoftSPI(baudrate=400000, polarity=1, phase=0, sck=sck, mosi=copi, miso=cipo)
display = Matrix8x8(spi, cs)
display.fill(0)
display.show()


        
def advancePixel():
    global col, row
    col = col + 1
    if col >= 8:
        col = 0
        row = row + 1
        if row >=8:
            row = 0

while(1):
    sleep(0.5)
    if row == 0 and col == 0:
        display.fill(0)
        display.show()
    display.pixel(col, row, 1)
    display.show()
    advancePixel()
    