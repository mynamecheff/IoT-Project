from imu import MPU6050 
import time
from machine import Pin, I2C
import umqtt_robust2 as mqtt
import adafruit_gps_main
import battery_percentage

i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
imu = MPU6050(i2c)
n = 0
x = 0
while True:
    try:
        for i in range(30):
            acceleration = imu.accel
            print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
                   "z: ", round(acceleration.z,2))

            
            if acceleration.z > 0.65:
                n = n+2
                print("you took " + str(n) + " steps")
                time.sleep(0.3)
                mqtt.web_print(n,'NamesJeff/feeds/Welcome Feed')
               
            elif abs(acceleration.x) > 0.8 or acceleration.z < -0.8:
                x = x+1
                print("you fell " + str(x) + " times")
                while acceleration.y < 0.9:
                    time.sleep(1)
           
                mqtt.web_print(x,'NamesJeff/feeds/ESP32Feed')
                if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
                    mqtt.besked = ""            
                    mqtt.sync_with_adafruitIO()
                    
            time.sleep(0.2)
        adafruit_gps_main.GPSmain()
        battery_percentage.Battery_mercy
    except KeyboardInterrupt:
            print('Ctrl-C pressed...exiting')
            mqtt.c.disconnect()
            mqtt.sys.exit()
