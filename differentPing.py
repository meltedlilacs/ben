#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_2.py
# Measure distance using an ultrasonic module
# in a loop.
#
# Author : Matt Hawkins
# Date   : 28/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------

def measure():
  print("at measure() top")
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  time.sleep(0.00006)
  start = time.time()
  print("waiting for echo pin to hit HIGH")
  while GPIO.input(GPIO_ECHO)==GPIO.LOW:
	start = time.time()
  print("waiting for echo pin to hit LOW")
  while GPIO.input(GPIO_ECHO)==GPIO.HIGH:
	stop = time.time()
  print("done timing")
  elapsed = stop-start
  distance = (elapsed * 34300)/2
  print("distance: " + distance)
  return distance

def measure_average():
  # This function takes 3 measurements and
  # returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 24
GPIO_ECHO    = 25

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:

  while True:

	distance = measure_average()
	print "Distance : %.1f" % distance
	time.sleep(1)

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
  print("\nSafely ending...")