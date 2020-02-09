# 10_proximity.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import DigitalOutputDevice, LED, Button
import time

# This project uses the Capsense technique modelled on this:
# http://playground.arduino.cc/Main/CapacitiveSensor


threshold = 0

# setup the pin modes
send_pin = DigitalOutputDevice(18)
sense_pin = Button(23, pull_up=None, active_state=True)
red_led = LED(24)
send_pin.on()

# return the time taken for the sense pin to flip state as a result of
# the capcitatve effect of being near the sense pin
def step():
    send_pin.off()
    t1 = time.time()
    while sense_pin.value:
        pass
    t2 = time.time()
    time.sleep(0.1)
    send_pin.on()
    time.sleep(0.1)
    return (t2 - t1) * 1000000

# This function takes 10 readings and finds the largest and puts it in the
# variable - threshold
def calibrate():
    global threshold
    print("Wait! Calibrating")
    n = 10
    maximum = 0
    for i in range(1, n):
        reading = step()
        if reading > maximum:
            maximum = reading
    threshold = maximum * 1.2
    print(threshold)
    print("Calibration Complete")


calibrate()

while True:
    reading = step() # take a reading
    red_led.value = (reading > threshold) # LED on if reading > threshold, otherwise off
