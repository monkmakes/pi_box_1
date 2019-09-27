# 10_water.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from gpiozero import LED, Button
import time

sense_pin = Button(18)

while True:
    print(sense_pin.is_pressed)
    time.sleep(0.1)