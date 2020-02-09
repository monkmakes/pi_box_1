# 01_blink.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import LED
from signal import pause

red_led = LED(18)

# The first number in blink() is the on time and the second is the off time (both in seconds)
red_led.blink(on_time=0.5, off_time=0.5)

pause()

# The pause() is needed at the end to keep the program running.
