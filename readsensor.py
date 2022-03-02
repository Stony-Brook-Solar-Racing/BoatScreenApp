import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
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
	#client = pymongo.MongoClient(mongodb_uri)
	#db = client.SolarRacingData
	#rpm = db.RPM
	
	# I2C Modules: Configuration and Setup
	i2c = busio.I2C(board.SCL, board.SDA)
	gps = adafruit_gps.GPS_GtopI2C(i2c)
	gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
	gps.send_command(b"PMTK220,1000")
	ads = ADS.ADS1115(i2c, address=0x49)
	ads_channel = AnalogIn(ads, ADS.P1)

	# Setup GPIO pins
	GPIO.setup(29, GPIO.IN)
	GPIO.cleanup()
	
	HIGH = True
	LOW = False
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(29, GPIO.IN) # GPIO 5 - ADC ALERT
	GPIO.setup(24, GPIO.IN) # GPIO 8 - GPS PPS
	GPIO.setup(16, GPIO.OUT) # GPIO 23 - MUX SELECT A
	GPIO.setup(18, GPIO.OUT) # GPIO 24 - MUX SELECT B
	
	# Testing
	try:
		while True:
			gps.update()
			print("GPS DATA\n" + "-" * 20)
			if gps.has_fix:
				print(
					"Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
					gps.timestamp_utc.tm_mon, # Grab parts of the time from the
						gps.timestamp_utc.tm_mday, # struct_time object that holds
						gps.timestamp_utc.tm_year, # the fix time. Note you might
						gps.timestamp_utc.tm_hour, # not get all data like year, day,
						gps.timestamp_utc.tm_min, # month!
						gps.timestamp_utc.tm_sec,
					)
				)
				print("Latitude: {0:.6f} degrees".format(gps.latitude))
				print("Longitude: {0:.6f} degrees".format(gps.longitude))
				print("Fix quality: {}".format(gps.fix_quality))
				# Some attributes beyond latitude, longitude and timestamp are optional
				# and might not be present. Check if they're None before trying to use!
				print("# satellites: {}".format(gps.satellites) if gps.satellites is not None else "# satellites: NO DATA")
				print("Altitude: {} meters".format(gps.altitude_m) if gps.altitude_m is not None else "Altitude: NO DATA")
				print("Speed: {} knots".format(gps.speed_knots) if gps.speed_knots is not None else "Speed: NO DATA")
				print("Track angle: {} degrees".format(gps.track_angle_deg) if gps.track_angle_deg is not None else "Track angle: NO DATA")
				print("Horizontal dilution: {}".format(gps.horizontal_dilution) if gps.horizontal_dilution is not None else "Horizontal dilution: NO DATA")
				print("Height geoid: {} meters".format(gps.height_geoid) if gps.height_geoid is not None else "Height geoid: NO DATA")
			else:
				print("Awaiting GPS fix...")
			print("-" * 20)
				
			print("MULTIPLEXER DATA\n" + "-" * 20)
			GPIO.output(16, LOW)
			GPIO.output(18, LOW)
			print("S1+: ", ads_channel.value)
			GPIO.output(16, HIGH)
			GPIO.output(18, LOW)
			print("S1-: ", ads_channel.value)
			s1minus = ads_channel.value
			voltage = (s1minus / 32767.0) * 6.144
			voltage = (voltage) 
			print("Voltage: ", voltage)
			GPIO.output(16, LOW)
			GPIO.output(18, HIGH)
			print("S2+: ", ads_channel.value)
			GPIO.output(16, HIGH)
			GPIO.output(18, HIGH)
			print("S2-: ", ads_channel.value)
			print("-" * 20 + "\n")
			time.sleep(1)
	finally:
		# Clear GPIO configurations and terminate
		GPIO.cleanup()
