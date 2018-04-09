"""
Sven Nelson
4/9/2018
RootBot Farmware to send GPIO high to 2nd raspberry pi
"""
# Need this for GPIO in/out
import RPi.GPIO as GPIO

from time import sleep

# Pin Definitions
fromCameraPi = 15 
toCameraPi = 14 

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(fromCameraPi, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(toCameraPi, GPIO.OUT, initial = GPIO.LOW)

# Send signal HIGH on pin 14 to initiate photo taking process
GPIO.output(toCameraPi, GPIO.HIGH)

# Check to see if the CameraPi has sent a HIGH to confirm photography complete
while GPIO.input(fromCameraPi) == 0:
    sleep(3)

# Send signal LOW on pin 14 until next time this script is run
GPIO.output(toCameraPi, GPIO.LOW)
		
# At end
GPIO.cleanup()
