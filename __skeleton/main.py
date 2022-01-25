from program import *
import sys
setup()

while(True):
    try:
        loop()
    except KeyboardInterrupt:
        print('program stopped')
        cleanup()
        sys.exit(0)