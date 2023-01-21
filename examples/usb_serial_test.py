import micropython
import sys
import select

from machine import Pin, UART
from machine import Timer

tmr = Timer(-1)

micropython.kbd_intr(-1)


# timed_serial = tmr.init(period = 500, mode = Timer.PERIODIC, callback = serial_ticker)
while(True):
    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        ch = sys.stdin.read(1)
        sys.stdout.write('>'+ch)