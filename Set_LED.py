#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys, getopt

# Initialise
pwm = PWM(0x40)
endPulse = 0  # Min pulse length out of 4096

# Set the brightness (up to 4096)
input = sys.argv[1]
powah = int(input)

# The magic
brightness = (4095-powah)
pwm.setPWMFreq(1000)                        # Set frequency to 60 Hz
pwm.setPWM(0, brightness, endPulse) # Channel, start pulse, end pulse



