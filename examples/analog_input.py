from machine import ADC, Pin
from time import sleep

light_sensor = ADC(28)

while True:
    light_level = light_sensor.read_u16()
    print(light_level)
    if(light_level < 1000):
        print('darkness upon us')
        sleep(3)
        
    sleep(0.1)