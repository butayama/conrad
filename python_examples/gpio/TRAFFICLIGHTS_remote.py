#!/usr/bin/env python
# https://gpiozero.readthedocs.io/en/stable/recipes.html
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep


factory = PiGPIOFactory(host='192.168.2.172')
led = LED(17, pin_factory=factory)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
