from machine import Pin, ADC
from time import sleep
import neopixel	
analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)
n = 0
np = neopixel.NeoPixel(Pin(12), 10)

analog_val = analog_pin.read()
volts = (analog_val * 0.00097176101) #multiplied by 5 for 2 batteries in series.
round(volts, 1)
battery_percentage = volts * 100 - 320
n =battery_percentage
if n <= 10:
    np[1] = (255, 0, 0, 128)
    np.write()
elif n >= 10 and n <= 20:
    for x in range(2):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 20 and n <= 30:
   for x in range(3):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 30 and n <= 40:
    for x in range(4):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 40 and n <= 50:
   for x in range(5):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 50 and n <= 60:
    for x in range(6):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 60 and n <= 70:
    for x in range(7):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 70 and n <= 80:
    for x in range(8):
        np[x] = (255, 0, 0, 128)
        np.write()
elif n >= 80 and n <= 90:
    for x in range(9):
        np[x] = (255, 0, 0, 128)
        np.write()
else:
    for x in range(10):
        np[x] = (255, 0, 0, 128)
        np.write()
sleep(0.5)
