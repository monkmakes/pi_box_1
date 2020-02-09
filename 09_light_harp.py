# 09_light_harp.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import DigitalOutputDevice
import time
from PiAnalog import *

pin1 = DigitalOutputDevice(24)
pin2 = DigitalOutputDevice(25)
p = PiAnalog()

def buzz(pitch, duration):
    period = 1.0 / pitch
    p2 = period / 2
    cycles = int(duration * pitch)
    for i in range(0, cycles):
        pin1.on()
        pin2.off()
        delay(p2)
        pin1.off()
        pin2.on()
        delay(p2)

def delay(p):
    t0 = time.time()
    while time.time() < t0 + p:
        pass

while True:
    reading = p.analog_read() # 1000 to 5000 ish for indoors
    f = reading * 2
    buzz(f, 0.1)
