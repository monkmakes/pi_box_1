# 06_reactions.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from gpiozero import RGBLED, Button
import time, random

rgb_led = RGBLED(red=18,green=23, blue=17) # Pin 17 is not connected but RGBLED() requires 3 pins
red_switch = Button(25)
green_switch = Button(24)

# find which buttons pressed 0 means neither, -1=both, 2=red, 1=green 
def key_pressed():
    # if button is pressed is_pressed will report false for that input
    if red_switch.is_pressed and green_switch.is_pressed:
        return -1
    if not red_switch.is_pressed and not green_switch.is_pressed:
        return 0
    if not red_switch.is_pressed and green_switch.is_pressed:
        return 1
    if red_switch.is_pressed and not green_switch.is_pressed:
        return 2

while True:
    rgb_led.off()
    print("Press the button for red or green when one lights")
    delay = random.randint(3, 7)    # random delay of 3 to 7 seconds
    color = random.randint(1, 2)    # random color red=1, green=2
    time.sleep(delay)
    if (color == 2):
        print("red")
        rgb_led.red = 1
    else:
        print("green")
        rgb_led.green = 1
    t1 = time.time()
    while not key_pressed():
        pass
    t2 = time.time()
    if key_pressed() != color :   # check the right buton was pressed
        print("WRONG BUTTON")
    else:
        # display the response time
        print("Time: " + str(int((t2 - t1) * 1000)) + " milliseconds")
