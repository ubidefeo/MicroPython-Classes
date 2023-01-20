from machine import Pin, PWM
from time import sleep_ms
from servo import Servo

SERVO_PIN_NUMBER = 21
servo_pin = PWM(Pin(SERVO_PIN_NUMBER))
servo_motor = Servo(servo_pin)

while(1):
    servo_motor.goto(0)
    sleep_ms(1000)
    servo_motor.goto(1024)
    sleep_ms(500)