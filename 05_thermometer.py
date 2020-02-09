# 05_thermometer.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from PiAnalog import *
from guizero import App, Text
import time

p = PiAnalog()

# Update the temperature reading
def update_temp():
    temperature = p.read_temp_c()
    temperature = "%.2f" % temperature # Round the temperature to 2 d.p. 
    temp_text.value = temperature
    temp_text.after(1000, update_temp)

# Create the GUI
app = App(title = "Thermometer", width="400", height="300")
Text(app, text="Temp C", size=32)
temp_text = Text(app, text="0.00", size=110)
temp_text.after(1000, update_temp) # Used to update the temperature reading
app.display()
