# 08_light_meter.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from guizero import App, Text
from PiAnalog import *
import time, math

p = PiAnalog()

def light_from_r(R):
    # Log the reading to compress the range
    return math.log(1000000.0/R) * 10.0 

# group together all of the GUI code
# Update the reading
def update_reading():
    light = light_from_r(p.read_resistance())
    reading_str = "{:.0f}".format(light)
    light_text.value = reading_str
    light_text.after(200, update_reading)

app = App(title="Light Meter", width="400", height="300")
Text(app, text="Light", size=32)
light_text = Text(app, text="0", size=110)
light_text.after(200, update_reading)
app.display()
