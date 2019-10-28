# 08_light_meter.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

from guizero import App, Text
from PiAnalog import *
import time, math

# This project uses a photoresistor, a component whose resistance varies with the light falling on it.
# To measure its resistance, the code records the time it takes for a capacitor to fill  
# when supplied by a current passing through the resistor. The lower the resistance the faster 
# it fills up. 
#
# You can think of a capacitor as a tank of electricity, and as it fills with charge, the voltage
# across it increases. We cannot measure that voltage directly, because the Raspberry Pi
# does not have an analog to digital convertor (ADC or analog input). However, we can time how long it
# takes for the capacitor to fill with charge to the extent that it gets above the 1.65V or so
# that counts as being a high digital input. 
# 
# For more information on this technique take a look at: 
# learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi
# The code here is based on that in the Raspberry Pi Cookbook (Recipes 12.1 to 12.3)

p = PiAnalog()

def read_resistance():
    n = 20
    total = 0;
    for i in range(1, n):
        total = total + p.analog_read()
    reading = total / float(n)
    resistance = reading * 6.05 - 939
    return resistance

def light_from_r(R):
    # Log the reading to compress the range
    return math.log(1000000.0/R) * 10.0 

# group together all of the GUI code
# Update the reading
def update_reading():
    light = light_from_r(read_resistance())
    reading_str = "{:.0f}".format(light)
    light_text.value = reading_str
    light_text.after(200, update_reading)

app = App(title="Light Meter", width="400", height="300")
Text(app, text="Light", size=32)
light_text = Text(app, text="0", size=110)
light_text.after(200, update_reading)
app.display()
