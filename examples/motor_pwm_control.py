# example to use with Sparkfun Dual Motor Driver TB6612FNG
# for wire hookup check documentation
# https://learn.sparkfun.com/tutorials/tb6612fng-hookup-guide
#
#
# details on Duty Cycle, Frequency, Pulse Width
# https://www.youtube.com/watch?v=rBQVfCUuhfs

from time import sleep_ms
from machine import Pin, PWM

base_freq = 80
base_duty_cycle = 0
# create a controllable PWM Pin
motor_right = PWM(Pin(19))
motor_left = PWM(Pin(20))

# speed between 12000 and 200000
# turn off with 0
def change_speed(speed):
    motor_right.freq(base_freq)
    motor_right.duty_u16(speed)
    motor_left.freq(base_freq)
    motor_left.duty_u16(speed)

change_speed(15000)
sleep_ms(700)
change_speed(30000)
sleep_ms(700)
change_speed(60000)
sleep_ms(700)
change_speed(120000)
sleep_ms(700)
change_speed(200000)
sleep_ms(700)
change_speed(0)
    
