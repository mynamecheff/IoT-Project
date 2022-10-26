from machine import Pin, ADC
from time import sleep

analog_pin = ADC(Pin(34))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)


while True:
    analog_val = analog_pin.read()
    print("Raw Analog Value: ", analog_val)
    volts = (analog_val * 0.00097176101)*5 #multiplied by 5 for 2 batteries in series.
    round(volts, 1)
    print("Voltage Value: ", round(volts, 2), "v")
    battery_percentage = volts * 100 - 320
    print("Rough Battery Percentage: ", round(battery_percentage, 1), "%")
    sleep(0.5)