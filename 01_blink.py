# 01_blink.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from gpiozero import LED
import time
from signal import pause

red_led = LED(18)

# The first number in blink() is the on time and the second is the off time (both in seconds)
red_led.blink(on_time=0.5, off_time=0.5)

pause()s

# The pause() is needed at the end to keep the program running.