# Arduino Nano pins to RP2040 pins

class InvalidPin(Exception):
    # Raised when user tries to initialise an invalid Pin
    pass

A0 = 'A0'
A1 = 'A1'
A2 = 'A2'
A3 = 'A3'
A4 = 'A4'
A5 = 'A5'
A6 = 'NA'
A7 = 'NA'

digital_pins = {0: 0, 1: 1, 2: 25, 3: 15, 4: 16, 5: 17, 6: 18, 7: 19, 8: 20, 9: 21, 10: 5, 11: 7, 12: 4, 13: 6}
analog_pins = {'A0': 26, 'A1': 27, 'A2': 28, 'A3': 29, 'A4': 12, 'A5': 13}

def nano_pin(pin_id):
    try:
        if(pin_id in digital_pins):
            return digital_pins[pin_id]
        if(pin_id in analog_pins):
            return analog_pins[pin_id]
        raise InvalidPin
    except InvalidPin:
        print('Pin not supported for the operation')
