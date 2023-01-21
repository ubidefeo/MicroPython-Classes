# Rotary Encoder example for Raspberry Pi Pico RP2

from rotary_irq_rp2 import RotaryIRQ
from time import sleep_ms

r_enc = RotaryIRQ(25, 15)

while(True):
    print(r_enc.value())
    sleep_ms(50)