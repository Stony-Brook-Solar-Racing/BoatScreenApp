import adafruit_gps
import board
import busio
import pymongo
import RPi.GPIO as GPIO
import time
from datetime import datetime

if __name__ == "__main__":
	# Setup MongoDB connection
	with open('auth.txt') as f:
		mongodb_uri = f.readline()
	client = pymongo.MongoClient(mongodb_uri)
	db = client.SolarRacingData
	rpm = db.RPM
	
	# I2C Modules: Configuration and Setup
	i2c = board.I2C()
	gps = adafruit_gps.GPS_GtopI2C(i2c)
	gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
	gps.send_command(b"PMTK220,1000")

	# Setup GPIO pins
	"""
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(29, GPIO.IN) # GPIO 5
	GPIO.setup(31, GPIO.OUT) # GPIO 6
	GPIO.setup(26, GPIO.OUT) # GPIO 7
	GPIO.setup(16, GPIO.OUT) # GPIO 23
	GPIO.setup(18, GPIO.OUT) # GPIO 24
	"""
	
	# Testing
	while True:
		data = gps.read(32)
		if not gps.has_fix:
			print("GPS has no fix!")
		elif data is not None:
			print("".join([chr(b) for b in data]))
	
	# Clear GPIO configurations and terminate
	GPIO.cleanup()
