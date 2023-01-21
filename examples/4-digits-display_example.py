from machine import Pin
from time import sleep
import tm1637

tm = tm1637.TM1637(clk=Pin(13), dio=Pin(12))

tm.write([63, 191, 63, 63])
sleep(1)

tm.numbers(17,23)
sleep(1)
tm.show('abcd')
sleep(1)
tm.show('bcde')
sleep(1)
tm.show('cdef')
sleep(1)

tm.temperature(20)