
# Rotary Encoder example for Raspberry Pi Pico RP2

from ht16k33matrixcolour import HT16K33MatrixColour
from machine import I2C
from rotary_irq_rp2 import RotaryIRQ
from time import sleep_ms
from Button import Button

from math import floor

r_enc = RotaryIRQ(25, 15, 0, 63, False, RotaryIRQ.RANGE_WRAP )

old_r_enc = r_enc.value()

i2c_bus = I2C(0)


selected_colour = 1
matrix_index = r_enc.value()

matrix = HT16K33MatrixColour(i2c_bus, 0x71)
matrix.set_brightness(2)
matrix.fill(0).draw()
matrix.plot(0, 0, 1).draw()

def index_to_row_col(index):
    row = 0
    col = 0
    row = floor(index / 8)

    col = (index % 8)
    print(row)
    print(col)
    return row, col
    
def button_action(pin, event):
    global selected_colour, matrix_index
    print('button pressed')
    if(event == Button.PRESSED):
        selected_colour = selected_colour + 1
        if(selected_colour > 3):
            selected_colour = 0
        row = index_to_row_col(matrix_index)[0]
        col = index_to_row_col(matrix_index)[1]
        matrix.plot(row, col, selected_colour).draw()
        

my_button = Button(16, callback = button_action, rest_state = False)

while(True):
    my_button.update()
    if(r_enc.value() != old_r_enc):
        matrix_index = r_enc.value()
        row = index_to_row_col(matrix_index)[0]
        col = index_to_row_col(matrix_index)[1]
        matrix.plot(row, col, selected_colour).draw()
        old_r_enc = r_enc.value()
        