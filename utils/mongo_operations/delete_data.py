from .connect import connect_mongo
from ..logger import log


log = log(log_for='utils/mongo_operations', log_file='delete_data.log')

def delete_Data(db, collection, email):
    """
    function delete_Data
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
        collection.delete_many({"email": email})
        log.write('data has been deleted', 'info')
        return True
    except Exception as e:
        log.write('data has not been deleted', 'error')
        return False, f'\n{e}'