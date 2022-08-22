from .send_data import send_Data
from ..data_validation.varify_colums import varify_data
import json
import pandas as pd
from .connect import connect_mongo
from ..logger import log
from .get_mails_from_db import get_data

log = log(log_for='utils/mongo_operations', log_file='upload_csv.log')


def upload_csv_file(db, collection, filename):
    """
    function upload_csv
    params:
        file: the file to be sent to the database
        db: the database name
        collection: the collection name
         
    returns:
        True: if the data is sent to the database
        False: if the data is not sent to the database
         
         
         
         
    """
    try:
        client = connect_mongo()
        mng_db = client[db]
        mng_collection = mng_db[collection]
        data = varify_data(filename=filename)
        
        #check if mail in data already exists in database
        existing_Data = get_data(db, collection)
        print(existing_Data)
        existing_Data = existing_Data['mail id'].tolist()
        existing_mail_index = []
        for mail in data['mail id']:
            if mail in existing_Data:
                indexes = data.index[data['mail id'] == mail]
                indexes = ''.join([str(value) for value in indexes])
                existing_mail_index.append(indexes)
        
        for index in existing_mail_index:
            data.drop(int(index), inplace=True)
                
        data = data.to_dict('records')
        print(data)
        # for i in data:



        # # data = pd.read_csv(data)
        # data_json = json.loads(data.to_json(orient='records'))
        
        mng_collection.insert_many(data)
        log.write('data has been inserted', 'info')
        return True
    except Exception as e:
        log.write('data has not been inserted', 'error')
        print(e)
        return False, f'\n{e}'