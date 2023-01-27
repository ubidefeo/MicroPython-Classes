# Rotary Encoder example for Raspberry Pi Pico RP2

from rotary_irq_rp2 import RotaryIRQ
from time import sleep_ms

# Encoder set to run between 0 and 10, rapping 10 > 0 and 0 > 10 
r_enc = RotaryIRQ(20, 19, min_val = 0, max_val = 10, range_mode = RotaryIRQ.RANGE_WRAP)

while(True):
    print(r_enc.value())
    sleep_ms(50)