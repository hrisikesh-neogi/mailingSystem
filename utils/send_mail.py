import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

import codecs

from utils.logger import log

log = log(log_for='send_mail', log_file='send_mail.log')

with open('config.json', 'r') as c:
    params = json.load(c)["params"]




class send_mails:
    def __init__(self, csv_path,subject, sender, message_body, link):
        self.csv_path = csv_path
        self.df = pd.read_csv(self.csv_path)
        
        self.emails = self.df['mail id'].tolist()
        self.names = self.df['name'].tolist()
        self.subject = subject
        self.sender = sender
        self.message_body = message_body
        self.link = link


    def main_function(self, name, email):
        server = sm.SMTP("smtp-mail.outlook.com", port=587)
        server.starttls()
        server.login(params['gmail-user'],params['gmail-password'])
        from_ = self.sender
        to_ =  email
        message = MIMEMultipart("alternative")
        message['Subject'] = self.subject
        message['from'] = self.sender
        file = codecs.open("templates/email.html", "r", "utf-8")
        html = file.read()
        html = html.replace("{{message}}", self.message_body)
        html = html.replace("{{name}}", name)
        html = html.replace("{{link}}", self.link)
        
        text  =  MIMEText(html, "html")
        
        message.attach(text)
        server.sendmail(from_,to_, message.as_string())
        log.write(f'message has been sent to the email \n id = {email}', 'info')

    def send_mails_to_recipients(self):
        for i in range(len(self.emails)):
            self.main_function(self.names[i], self.emails[i])
        log.write(f'message has been sent to the email \n id = {self.emails[i]}', 'info')
    
        
        print("message has been sent to the emails")