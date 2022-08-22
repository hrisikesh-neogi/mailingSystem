from .connect import connect_mongo
from ..logger import log
import pandas as pd

log = log(log_for='utils/mongo_operations', log_file='get_data.log')

def get_data(db, collection):
    """
    function get_data
    params:
        db: the database name
        collection: the collection name
        query: the query to be sent to the database
            
            returns:
                True: if the data is deleted from the database
                False: if the data is not deleted from the database
                
                """
    try:
        client = connect_mongo()
        db = client[db]
        collection = db[collection]
        data = collection.find({})
        data = pd.DataFrame(list(data))
        return data
    except Exception as e:
        log.write('data has not been deleted', 'error')
        print("the error is here in get ")
        return False, f'\n{e}'