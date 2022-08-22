from ..logger import log
import json
import pymongo 
import os

log_folder = ''
log = log(log_for='utils/mongo_operations', log_file='connect.log')

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

def connect_mongo():
    try:
        client = pymongo.MongoClient(params['mongo_url'])
        log.write('mongo client is connected', 'info')
        return client
    except pymongo.errors.ConnectionFailure as e:
        log.write('mongo client is not connected', 'error')
        return False
