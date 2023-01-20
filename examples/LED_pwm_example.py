# details on Duty Cycle, Frequency, Pulse Width
# https://www.youtube.com/watch?v=rBQVfCUuhfs


from machine import Pin, PWM

# start fresh: reset the Pin
dimmable_led.deinit()

# create a controllable Pin
dimmable_led = PWM(Pin(6))
# dimmable_led.freq(10)
# dimmable_led.duty_u16(5000)
