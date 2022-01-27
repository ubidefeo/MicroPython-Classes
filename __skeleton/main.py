from arduino import *
from arduino_utils import ArduinoPin as Pin
from arduino_utils import *
import sys
setup()

while(True):
    try:
        loop()
    except KeyboardInterrupt:
        print('program stopped')
        cleanup()
        sys.exit(0)