from machine import Pin
from machine import I2C



from time import sleep
import tm1637
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

import i2c_lcd
i2c = I2C(id=0, scl=Pin(13), sda=Pin(12))
lcd = i2c_lcd.Display(i2c)


tm = tm1637.TM1637(clk=Pin(25), dio=Pin(15))
myPin = Pin(25, Pin.OUT)
tm.write([127, 255, 127, 127])
hola = [118, 63, 56, 119]
ciao = [57, 48, 119, 63]
flipflop = False
col = 0
row = 0

def tgl():
    global flipflop, hola, ciao
    myPin.toggle()
    flipflop = ~flipflop
    lcd.clear()
    if(flipflop):
        tm.write(hola)
        lcd.home();
        lcd.write('Hola, Mundo!')
    else:
        tm.write(ciao)
        lcd.home();
        lcd.write('Hello, World!')
        

def advancePixel():
    global col, row
    col = col + 1
    if col >= 8:
        col = 0
        row = row + 1
        if row >=8:
            row = 0

while(1):
    tgl()
    sleep(0.5)
    if row == 0 and col == 0:
        display.fill(0)
        display.show()
    display.pixel(col, row, 1)
    display.show()
    advancePixel()
    