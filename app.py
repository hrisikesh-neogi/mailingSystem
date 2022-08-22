from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
import os
from utils.email import Email_receiver 
from utils.send_mail import send_mails
from utils.logger import log
from utils.mongo_operations.upload_csv import upload_csv_file

log = log(log_for='home', log_file='app.log')

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)




@app.route("/")
def index():
    log.write('index page is being accessed', 'info')
    return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        log.write('upload page is being accessed', 'info')
        
        file = ''.join([file for file in os.listdir("uploads")])
        
        if len(file)!=0:
            
            file_path = "uploads/"+file 
            os.remove(file_path)
            log.write('old file has been deleted', 'info')
            #new file read
            f = request.files['file']
            f.save(os.path.join('uploads', f.filename))
            log.write('file has been uploaded', 'info')
            
            
        else:
            file_path = "uploads/" 
            log.write('old file has been deleted', 'info')
            #new file read
            f = request.files['file']
            f.save(os.path.join('uploads', f.filename))
            log.write('file has been uploaded', 'info')
        
        filename = f.filename

        upload_csv_file(db = 'test', collection = 'test', filename=filename)
        log.write('csv file has been uploaded', 'info')
        return redirect("/email_sending")
    else:
        log.write('upload page is being accessed --> rendering the upload.html template', 'info')
        return render_template('upload.html')





@app.route("/email_sending", methods = ['GET', 'POST'])
def email_sending():

    # def send_mail_flask(to,subject,sender, name, message):

    #     msg = Message(subject=subject,sender=sender, recipients=to)
    #     msg.body = f"Hello {name} \n {message}"
    #     msg.html = render_template('email.html')
    #     mail.send(msg)



    if(request.method=='POST'):
        log.write('email sending page is being accessed', 'info')
    
        file = ''.join([file for file in os.listdir("uploads")])
        csv_path = "uploads/"+file 
        data = {key:value for key, value in request.form.items() }
        subject = data['subject']
        message = data['message']
        link = data['Link']
        

        msg_send = send_mails(csv_path, subject, params['gmail-user'], message, link)
        msg_send.send_mails_to_recipients()
        log.write('message has been sent to the emails', 'info')
        


        
        return render_template('emailSuccess.html')

    else:
        log.write('email sending page is being accessed --> rendering the email.html template', 'info')

        return render_template('email_sending.html', params=params)






# @app.route("/redirect_to_link", methods = ['GET', 'POST'])
# def redirect_to_link():
#     if(request.method=='POST'):
#         log.write('redirect_to_link page is being accessed', 'info')
#         return redirect(link)







if __name__ == '__main__':
    app.run(debug=True)