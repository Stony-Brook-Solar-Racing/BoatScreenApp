import adafruit_gps
import board
import busio
import pymongo
import RPi.GPIO as GPIO
import time
from datetime import datetime
import Adafruit_ADS1x15

if __name__ == "__main__":
    # Setup MongoDB connection
    with open('auth.txt') as f:
        mongodb_uri = f.readline()
    client = pymongo.MongoClient(mongodb_uri)
    db = client.SolarRacingData
    rpm = db.RPM

    print("GPIO")
    print(GPIO.getmode())
    if (GPIO.getmode() != 10):
        GPIO.setup(24,GPIO.IN)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        print("GPIO")
        print(GPIO.getmode())
    # I2C Modules: Configuration and Setup
    #i2c = board.I2C()
    #gps = adafruit_gps.GPS_GtopI2C(i2c)
    #gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    #gps.send_command(b"PMTK220,1000")

    # Setup GPIO pins
    #GPIO.cleanup()

    GPIO.setup(29, GPIO.IN) # GPIO 5
    GPIO.setup(31, GPIO.OUT) # GPIO 6
    GPIO.setup(26, GPIO.OUT) # GPIO 7
    GPIO.setup(16, GPIO.OUT) # GPIO 23
    GPIO.setup(18, GPIO.OUT) # GPIO 24
    
    HIGH = True
    LOW = False
    adc = Adafruit_ADS1x15.ADS1115()

    GAIN=2/3

    adc.start_adc(0,gain=GAIN)

    # Testing
    while True:
        #data = gps.read(32)
        #if not gps.has_fix:
            #print("GPS has no fix!")
        #elif data is not None:
            #print("".join([chr(b) for b in data]))
        print("TEST DATA")
        print(GPIO.input(29))
        
        print('Reading ADS1x15 channel for 1 for 5 seconds...')

        start=time.time()
        while(time.time() - start) <=5.0:
            value = adc.get_last_result()
            print('Channel 0: {0}'.format(value))
            time.sleep(0.5)

        adc.stop_adc()
        time.sleep(5)
        GPIO.output(18, LOW)
        GPIO.output(16, LOW)
        print("S1+")
        print(GPIO.input(29))
        print('Reading ADS1x15 channel for 1 for 5 seconds...')

        start=time.time()
        while(time.time() - start) <=5.0:
            value = adc.get_last_result()
            print('Channel 0: {0}'.format(value))
            time.sleep(0.5)

        adc.stop_adc()
        time.sleep(5)
        GPIO.output(18, LOW)
        GPIO.output(16, HIGH)
        print("S1-")
        print(GPIO.input(29))
        print('Reading ADS1x15 channel for 1 for 5 seconds...')

        start=time.time()
        while(time.time() - start) <=5.0:
            value = adc.get_last_result()
            print('Channel 0: {0}'.format(value))
            time.sleep(0.5)

        adc.stop_adc()
        time.sleep(5)
        GPIO.output(18, HIGH)
        GPIO.output(16, LOW)
        print("S2+")
        print(GPIO.input(29))
        print('Reading ADS1x15 channel for 1 for 5 seconds...')

        start=time.time()
        while(time.time() - start) <=5.0:
            value = adc.get_last_result()
            print('Channel 0: {0}'.format(value))
            time.sleep(0.5)

        adc.stop_adc()
        time.sleep(5)
        GPIO.output(18, HIGH)
        GPIO.output(16, HIGH)
        print("S2-")
        print(GPIO.input(29))
        print('Reading ADS1x15 channel for 1 for 5 seconds...')

        start=time.time()
        while(time.time() - start) <=5.0:
            value = adc.get_last_result()
            print('Channel 0: {0}'.format(value))
            time.sleep(0.5)

        adc.stop_adc()
        time.sleep(5)
    # Clear GPIO configurations and terminate
    GPIO.cleanup()
