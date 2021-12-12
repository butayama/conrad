#!/usr/bin/env python
from signal import pause
from gpiozero import PWMLED, Button

led = PWMLED(17)
dty_cyc = 0.1
button = Button(2)
led.value = dty_cyc


def incr_duty_cycle():
    global dty_cyc
    if dty_cyc == 0.8:
        dty_cyc = 0.1
    dty_cyc = dty_cyc * 2
    led.value = dty_cyc


button.when_pressed = incr_duty_cycle

pause()
