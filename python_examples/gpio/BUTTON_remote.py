#!/usr/bin/env python
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory


factory = PiGPIOFactory(host='192.168.2.172')
button = Button(2, pin_factory=factory)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
