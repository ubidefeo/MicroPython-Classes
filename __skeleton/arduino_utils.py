# Arduino Nano pins to RP2040 pins
from machine import Pin

A0 = 14
A1 = 15
A2 = 16
A3 = 17
A4 = 18
A5 = 19
A6 = 20
A7 = 21

board_pins = {0: 0, 1: 1, 2: 25, 3: 15, 4: 16, 5: 17, 6: 18, 7: 19, 8: 20, 9: 21, 10: 5, 11: 7, 12: 4, 13: 6, A0: 26, A1: 27, A2: 28, A3: 29, A4: 12, A5: 13, A6: -1, A7: -1}

class ArduinoPin(Pin):
    def __init__(self, pin_id, mode, pull = None):
        hardware_pin = board_pins[pin_id]
        self.pin = Pin(hardware_pin, mode, pull)

    def on(self):
        self.pin.on()

    def off(self):
        self.pin.off()

    def toggle(self):
        self.pin.toggle()