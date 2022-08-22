from .connect import connect_mongo
from ..logger import log

log = log(log_for='utils/mongo_operations', log_file='send_Data.log')

def send_Data(data, db, collection):
    """
    function send_Data
    params:
        data: the data to be sent to the database
        db: the database name
        collection: the collection name

    returns:
        True: if the data is sent to the database
        False: if the data is not sent to the database

    
    
    
    """
    try:
        client = connect_mongo()
        db = client[db]
        collection = db[collection]
        collection.insert_one(data)
        log.write('data has been inserted', 'info')
        return True
    except Exception as e:
        log.write('data has not been inserted', 'error')
        return False, f'\n{e}'




