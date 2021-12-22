#!/usr/bin/env python
# https://gpiozero.readthedocs.io/en/stable/recipes.html
from gpiozero import LEDBarGraph
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.2.172')
graph = LEDBarGraph(5, 6, 13, 19, 26, pin_factory=factory)
weiter = True


class UnknownException(Exception):
    pass


def led_aus(gv=0):
    return gv

try:
    while weiter:
        graph.value = 1  # (1, 1, 1, 1, 1)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = 1 / 5  # (1, 0, 0, 0, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = 2 / 5  # (1, 1, 0, 0, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = 3 / 5  # (1, 1, 1, 0, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = 4 / 5  # (1, 1, 1, 1, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = 5 / 5  # (1, 1, 1, 1, 1)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = -1  # (1, 1, 1, 1, 1)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = -1 / 5  # (1, 0, 0, 0, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = -2 / 5  # (1, 1, 0, 0, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = -3 / 5  # (1, 1, 1, 0, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = -4 / 5  # (1, 1, 1, 1, 0)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        graph.value = -5 / 5  # (1, 1, 1, 1, 1)
        sleep(1)
        graph.value = led_aus()
        sleep(0.5)
        answer = input('Weiter J/N')
        if answer in ("N", "n"):
            weiter = False

except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    print(f"graph.value = {graph.value}")

except UnknownException:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
    raise UnknownException("UnknownException occured")

finally:
    graph.value = 0  # (0, 0, 0, 0, 0, 0)

graph.value = 0  # (0, 0, 0, 0, 0, 0)