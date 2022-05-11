from pymongo import MongoClient
import pymongo

def get_rpm():
    f = open('./data/databaseurl.txt', 'r')
    URL = f.read()
    client = MongoClient(URL)
    db = client["SolarRacingData"]
    collection = db['RPM']
    rpm = collection.find().sort('ISOString', pymongo.DESCENDING)[0]
    return rpm

def get_voltage_data():
    f = open('./data/databaseurl.txt', 'r')
    URL = f.read()
    client = MongoClient(URL)
    db = client["SolarRacingData"]
    collection = db['Voltage']
    voltage = collection.find().sort('ISOString', pymongo.DESCENDING)[0]
    return voltage

def get_v_res():
    return get_voltage_data()['voltage']

def get_s1minus():
    return get_voltage_data()['s1minus']    
   
def get_s1plus():
    return get_voltage_data()['s1plus']

def get_s2minus():
    return get_voltage_data()['s2minus']

def get_s2plus():
    return get_voltage_data()['s2plus']

def get_gps_data():
    f = open('./data/databaseurl.txt', 'r')
    URL = f.read()
    client = MongoClient(URL)
    db = client["SolarRacingData"]
    collection = db['Voltage']
    voltage = collection.find().sort('ISOString', pymongo.DESCENDING)[0]
    return voltage

def get_speed():
    return get_gps_data()['speed']