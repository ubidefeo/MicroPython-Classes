from machine import SoftI2C, Pin
import ssd1306_1315 as ssd1306

from Button import Button

DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64

i2cbus = SoftI2C(scl = Pin(13), sda = Pin(12), freq = 100000)
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2cbus)

counter = 0

def clear_screen():
    oled.fill(0)
    oled.show()

oled.text("ciao", 0, 0, 1)
oled.show()


def button_action(pin, event):
    global counter, oled

    print('button action')
    print(pin)
    if event == Button.PRESSED:
        print('pressed')
        counter = counter + 1
        print(counter)
        clear_screen()
        oled.text(f'counter: {counter}', 0, 0, 1)
        oled.pixel(counter, counter, 1)
        oled.show()
        
    if event == Button.RELEASED:
        print('released')
    
my_button = Button(18, callback = button_action)

while(True):
    my_button.update()
    
    
    
    
    
    
    
    
    
    
    
    
    