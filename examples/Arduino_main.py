from time import sleep_ms
def setup():
    print('Start')

    
def loop():
    print('loop')
 
setup()
while(1):
    loop()
    sleep_ms(100)