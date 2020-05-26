# 07_reactions.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import LED, Button
import time, random

left_led = LED(25)
right_led = LED(23)
left_switch = Button(24)
right_switch = Button(18)

# find which buttons pressed 0 means neither, -1=both, 2=right, 1=left
def key_pressed():
    # if button is pressed is_pressed will report false for that input
    if left_switch.is_pressed and right_switch.is_pressed:
        return -1
    if not left_switch.is_pressed and not right_switch.is_pressed:
        return 0
    if not right_switch.is_pressed and left_switch.is_pressed:
        return 1
    if right_switch.is_pressed and not left_switch.is_pressed:
        return 2

while True:
    left_led.off()
    right_led.off()
    print("Press the button next to the LED that lights up")
    delay = random.randint(3, 7)    # random delay of 3 to 7 seconds
    led = random.randint(1, 2)    # random led left=1, right=2
    time.sleep(delay)
    if (led == 1):
        print("left")
        left_led.on()
    else:
        print("right")
        right_led.on()
    t1 = time.time()
    while not key_pressed():
        pass
    t2 = time.time()
    if key_pressed() != led :   # check the correct button was pressed
        print("WRONG BUTTON")
    else:
        # display the response time
        print("Time: " + str(int((t2 - t1) * 1000)) + " milliseconds")
