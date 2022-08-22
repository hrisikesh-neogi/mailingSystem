import pandas as pd
import os
import json
import re
from ..logger import log

log = log(log_for='utils/data_validation', log_file='varify_colums.log')

# data = os.listdir('uploads')
# data = [file for file in data if file.endswith('.csv')]


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    if(re.search(regex,email)):   
        return True  
    else:   
        return False

def  varify_data(filename):
    df = pd.read_csv('uploads/'+filename)
    columns = df.columns.tolist()
    for column in columns:
        column_data = df[column].tolist()
        varification = []
        for value in column_data:
            if check(value):
                varification.append(True)
            else:
                varification.append(False)

        if all(varification):
            df['mail id'] = df[column]
            
            
            
        else:
            df['name'] = df[column]
            

    log.write('data has been verified', 'info')
    os.remove('uploads/'+filename)
    df.to_csv('uploads/'+filename, index=False)
    log.write('data has been saved', 'info')
    
    return df


        

            
    