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
