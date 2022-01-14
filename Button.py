from machine import Pin

class Button(object):
    
    rest_state = False
    # pin = None
    # pin_number = 0
    RELEASED = 'released'
    PRESSED = 'pressed'
    def __init__(self, pin, rest_state = False, callback = None):
        self.pin_number = pin
        self.pin = Pin(pin, Pin.IN)
        self.rest_state = rest_state
        self.callback = callback
        self.active_state = False
    
    def update(self):
        # print(self.pin.value())
        if self.pin.value() == (not self.rest_state) and (not self.active_state):
            self.active_state = True
            if self.callback != None:
                self.callback(self.pin_number, Button.PRESSED)
            return
        if self.pin.value() == self.rest_state and self.active_state:
            self.active_state = False
            if self.callback != None:
                self.callback(self.pin_number, Button.RELEASED)
            return
    