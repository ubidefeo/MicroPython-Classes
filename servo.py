from machine import Pin, PWM

class Servo:
    def __init__(self, pin: int or Pin or PWM, minVal=2500, maxVal=7500):
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        if isinstance(pin, PWM):
            self.__pwm = pin
            self.__pwm.freq(50)
            self.minVal = minVal
        self.maxVal = maxVal

    def deinit(self):
        self.__pwm.deinit()

    def goto(self, value: int):
        if value < 0:
            value = 0
        if value > 1024:
            value = 1024
        delta = self.maxVal-self.minVal
        target = int(self.minVal + ((value / 1024) * delta))
        self.__pwm.duty_u16(target)

    def middle(self):
        self.goto(512)

    def free(self):
        self.__pwm.duty_u16(0)