'''
Using IMU to messure if someone has fallen and count it!
To use install the advanced IMU lib
TODO: stepcounter (minus the first value with the second and compare with a defined number)
'''

from imu import MPU6050 
import time
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)
n = 0

while True:
    acceleration = imu.accel
    
    print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
           "z: ", round(acceleration.z,2))

    if abs(acceleration.x) > 0.8 or abs(acceleration.z) > 0.8:
        n = n+1
        print("you fell " + str(n) + " times")
        while acceleration.y < 0.9:
            time.sleep(1)
    time.sleep(0.2)