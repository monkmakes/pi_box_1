# 09_light_harp.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from gpiozero import Buzzer
import time, math
from PiAnalog import *


buzzer = Buzzer(24)

p = PiAnalog()


# This function makes the tone on the buzzer
# by turning it on and off, with a delay caused by charge_time.
# Cunning or what?
def buzz():
    p.discharge()
    buzzer.on()
    p.discharge()
    p.charge_time()
    buzzer.off()
    p.charge_time()

while True:
    buzz()
