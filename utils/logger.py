import datetime
import os

log_dir ='logs'


class log:
    """
    class log

    takes -------------------------------------------------------------------->

    log_for:
        purpose : to log the data
        
    log_file: 
         purpose  :the file to log the data

    params:
        
        log_type: the type of log file
        log_for : name of the file the file that's logs are getting fetched

    exmple:
        log_for = 'home'
        log_file = 'home.log'
        log_type = 'logs'
        log = log(log_for, log_file, log_type)
        log.write('this is a log')

    
    
    
    """

    def __init__(self,log_for, log_file):
        self.log_file = log_file
        self.log_for = log_for
        

    def write(self, message, log_type):
        if self.log_for in os.listdir(log_dir):
            with open(log_dir+'/'+self.log_for+'/'+self.log_file, 'a') as f:
                f.write(f'{datetime.datetime.now()} {message}\n')
           
        else:
            file = log_dir+'/'+self.log_for
            if not os.path.exists(file):
                os.mkdir(log_dir+'/'+self.log_for)
            
        log_fname = os.path.join(log_dir+'/'+self.log_for, self.log_file)
        
        if os.path.exists(log_fname):
            mode = 'a' 
        else:
            mode = 'w'


        with open(log_fname, mode) as f:
            f.write(str(datetime.datetime.now()) + ': ' + log_type+'-->'+ message + '\n')