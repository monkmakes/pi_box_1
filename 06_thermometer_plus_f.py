from PiAnalog import *
from guizero import App, Text
from gpiozero import Buzzer
import time

set_temp = 77 # 77 in degrees F

buzzer = Buzzer(24)

def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)
    buzzer.beep(on_time=period, off_time=period, n=int(cycles/2))

p = PiAnalog()

# Update the temperature reading
def update_temp():
    temperature = p.read_temp_f()
    if temperature > set_temp:
        buzz(1000, 0.3)
    temperature = "%.2f" % temperature # Round the temperature to 2 d.p. 
    temp_text.value = temperature
    temp_text.after(1000, update_temp)

# Create the GUI
app = App(title = "Thermometer", width="400", height="300")
Text(app, text="Temp F", size=32)
temp_text = Text(app, text="0.00", size=110)
temp_text.after(1000, update_temp) # Used to update the temperature reading
app.display()
