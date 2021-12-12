#!/usr/bin/env python
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

# from signal import pause
# https://github.com/vibora-io/vibora/issues/183
# Library is not compatible with Windows due to not having signal.pause.

factory = PiGPIOFactory(host='192.168.2.172')

button = Button(2, pin_factory=factory)


def button_down(b_pressed=True):
    return b_pressed


def button_up(b_pressed=False):
    return b_pressed


def say_hello():
    print("Hello!")


def say_bye():
    print("Tschüss!")

pressed = False
while True:
    input("Press the button")
    button.when_pressed = say_hello
    button.when_released = say_bye


