# 06_thermometer_plus.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from PiAnalog import *
from guizero import App, Text
from gpiozero import DigitalOutputDevice
import time

set_temp = 25

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

# Update the temperature reading
def update_temp():
    temperature = p.read_temp_c()
    if temperature > set_temp:
        buzz(2000, 0.5)
    temperature = "%.2f" % temperature # Round the temperature to 2 d.p.
    temp_text.value = temperature
    temp_text.after(1000, update_temp)

# Create the GUI
app = App(title = "Thermometer", width="400", height="300")
Text(app, text="Temp C", size=32)
temp_text = Text(app, text="0.00", size=110)
temp_text.after(1000, update_temp) # Used to update the temperature reading
app.display()
