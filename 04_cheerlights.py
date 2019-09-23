from gpiozero import Button, RGBLED
from colorzero import Color
from signal import pause
import time, random, requests

led = RGBLED(red=18, green=23, blue=24)
button = Button(25, hold_time=2)

cheerlights_url = "http://api.thingspeak.com/channels/1417/field/2/last.txt"
cheer_colors = ["#FF0000", "#008000", "#0000FF", "#00FFFF", "#FFFFFF", "#FDF5E6", "#800080", "#FF00FF", "#FFFF00", "#FFA500", "#FFC0CB"]

def pressed():
    color_index = random.randint(0, 10)
    color = cheer_colors[color_index]
    print(color)
    led.color = Color(color)

def held():
    try:
        cheerlights = requests.get(cheerlights_url)
        color = cheerlights.content
        print(color)
        led.color = Color(color)
    except Exception as e:
        print(e)
    time.sleep(1)

button.when_pressed = pressed
button.when_held = held

pause()
