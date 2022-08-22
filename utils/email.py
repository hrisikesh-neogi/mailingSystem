import pandas as pd

class Email_receiver:
    def __init__(self, csv_path) :
        self.csv_path = csv_path
        self.df = pd.read_csv(self.csv_path)
        self.df.dropna(inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        
    def recepient_list(self):
        return self.df['mail id'].tolist(), self.df['name'].tolist()
