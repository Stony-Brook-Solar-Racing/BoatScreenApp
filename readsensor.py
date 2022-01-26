import pymongo
import RPi.GPIO as GPIO
from datetime import datetime

if __name__ == "__main__":
	# Setup MongoDB connection
	with open('auth.txt') as f:
		mongodb_uri = f.readline()
	client = pymongo.MongoClient(mongodb_uri)
	db = client.SolarRacingData
	rpm = db.RPM
	
	# Setup GPIO pins
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(29, GPIO.IN) # GPIO 5
	GPIO.setup(31, GPIO.OUT) # GPIO 6
	GPIO.setup(26, GPIO.OUT) # GPIO 7
	GPIO.setup(16, GPIO.OUT) # GPIO 23
	GPIO.setup(18, GPIO.OUT) # GPIO 24
	
	# Testing
	print(rpm.find().sort('ISOString', pymongo.DESCENDING)[0]);
	
	# Clear GPIO configurations and terminate
	GPIO.cleanup()
