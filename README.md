# IoT-Project
Items needed:
Esp32 or similar 
IMU (MPU6050)
GPS module(GY-NEO6MV2)
5v battery or two batteries inseries regulated by an LDO 

# Setup:
Battery mesurement is calculated with two batteries in series regulated by an LDO
change values in main.py and adafruit_gpsmain.py to match your io.adafruit feed

# How to run:
Connect batteries to pin 34.
connect the GPS to pin 16
connect IMU to pin 22 for SDA and 21 for STA
run main 
