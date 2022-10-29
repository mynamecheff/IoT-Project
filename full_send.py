from imu import MPU6050 
import time
from machine import Pin, I2C
import umqtt_robust2 as mqtt
import adafruit_gps_main
import vectorIMU
import uasyncio

async def main():
    n = 0
    x = 0
    while True:
        uasyncio.create_task(adafruit_gps_main.GPSmain())
        uasyncio.create_task(vectorIMU.stepNfall(n, x))

uasyncio.run(main)