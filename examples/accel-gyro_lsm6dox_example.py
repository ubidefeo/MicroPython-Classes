from time import sleep_ms
from lsm6dsox import LSM6DSOX as IMU
from machine import I2C

imu = IMU(I2C(0))

def read_values():
    gyro_x = imu.read_gyro()[0]
    gyro_y = imu.read_gyro()[1]
    gyro_z = imu.read_gyro()[2]

    print(gyro_x)
    print(gyro_y)
    print(gyro_z)
    
    print(f'x: {gyro_x:>8.3f}')
    print(f'y: {gyro_y:>8.3f}')
    print(f'z: {gyro_z:>8.3f}')

while True:
    read_values()
    sleep_ms(100)