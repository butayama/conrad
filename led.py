#!/usr/bin/env python
import gpiod
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, 1)
time.sleep(2)
GPIO.output(25, 0)
GPIO.cleanup()