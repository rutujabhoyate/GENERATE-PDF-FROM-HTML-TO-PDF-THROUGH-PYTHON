   
############################ GENERATE PDF FROM HTML TO PDF THROUGH PYTHON #########################################

'''from flask import Flask, render_template, send_file
from weasyprint import HTML
import os

app = Flask(__name__)

# Set the download path on the server
#Define the path where the generated PDF will be saved (download_path). Also, specify the path to the WeasyPrint binary (weasyprint_binary_path).
download_path = 'D:/NOV/Python_PDF'
os.makedirs(download_path, exist_ok=True)

weasyprint_binary_path = 'C:/Program Files/GTK3-Runtime Win64/bin/weasyprint.exe'

@app.route('/')
def index():
    # Render HTML template with Flask's render_template function
    rendered_template = render_template('index.html')

    # Generate PDF from rendered HTML using WeasyPrint
    pdf_path = os.path.join(download_path, 'output.pdf')
    #HTML(string=rendered_template).write_pdf(pdf_path)
    
    """Combine the rendered HTML with WeasyPrint to generate a PDF. The HTML class from WeasyPrint is used to create an HTML object
    from the rendered template, and then the write_pdf method is called to write the PDF to the specified path (pdf_path)"""
    HTML(string=rendered_template).write_pdf(pdf_path, weasyprint=weasyprint_binary_path)


    # Send the saved PDF as a response
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)'''
    
    

 
#######################################Multiple recipients##################################    
from flask import Flask, render_template, send_file
from weasyprint import HTML
import os
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'rutuja.myfirstplacement@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'ppvk mqvi erqm zsmh'  # Repla
app.config['MAIL_DEFAULT_SENDER'] = 'rutuja.myfirstplacement@gmail.com'  # Replace with a default sender email



# Set the download path on the server
download_path = 'D:/NOV/Python_PDF'
os.makedirs(download_path, exist_ok=True)

mail = Mail(app)

weasyprint_binary_path = 'C:/Program Files/GTK3-Runtime Win64/bin/weasyprint.exe'

# Flag to track whether the email has been sent
email_sent = False

# Define pdf_path outside the if block to avoid UnboundLocalError
pdf_path = os.path.join(download_path, 'output.pdf')

@app.route('/')
def index():
    global email_sent

    if not email_sent:
        # Render HTML template with Flask's render_template function
        rendered_template = render_template('index.html')

        # Generate PDF from rendered HTML using WeasyPrint
        HTML(string=rendered_template).write_pdf(pdf_path, weasyprint=weasyprint_binary_path)

        # Send the saved PDF as an email attachment with CC and BCC
        send_email(
            to='rutujabhoyate1510@gmail.com',
            cc=['archana.myfirstplacement@gmail.com','sanika.myfirstplacement@gmail.com'],
            bcc=['akshadrathod.myfirstplacement@gmail.com'],
            subject='PDF Subject',
            body='This is the body of the email',
            attachments=[pdf_path]
        )

        # Update the flag to indicate that the email has been sent
        email_sent = True

    # Send the saved PDF as a response
    return send_file(pdf_path, as_attachment=True)


'''@app.route('/')
def index():
    global email_sent

    if not email_sent:
        # Render HTML template with Flask's render_template function
        rendered_template = render_template('index.html')

        # Generate PDF from rendered HTML using WeasyPrint
        HTML(string=rendered_template).write_pdf(pdf_path, weasyprint=weasyprint_binary_path)

        # Send the saved PDF as an email attachment
        send_email('rutujabhoyate1510@gmail.com', 'PDF Subject', 'This is the body of the email', [pdf_path])

        # Update the flag to indicate that the email has been sent
        email_sent = True

    # Send the saved PDF as a response
    return send_file(pdf_path, as_attachment=True)

def send_email(to, subject, body, attachments=[]):
    msg = Message(subject, recipients=[to], body=body)
    for attachment in attachments:
        with app.open_resource(attachment) as attachment_file:
            msg.attach('output.pdf', 'application/pdf', attachment_file.read())
    mail.send(msg)'''
    
def send_email(to, subject, body, cc=None, bcc=None, attachments=[]):
    msg = Message(subject, recipients=[to], body=body, cc=cc, bcc=bcc)

    for attachment in attachments:
        with app.open_resource(attachment) as attachment_file:
            msg.attach('output.pdf', 'application/pdf', attachment_file.read())

    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
"""from flask import Flask
from flask_mail import Mail, Message
import sched
import time
from datetime import datetime, timedelta

app = Flask(__name__)


mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'rutuja.myfirstplacement@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'ppvk mqvi erqm zsmh'  # Repla
app.config['MAIL_DEFAULT_SENDER'] = 'rutuja.myfirstplacement@gmail.com'  # Replace with a default sender email



s = sched.scheduler(time.time, time.sleep)

def send_email():
    with app.app_context():
        msg = Message(
            'Scheduled Email',
            recipients=['rutujabhoyate1510@gmail.com'],  # Replace with the recipient's email
            body='This is a scheduled email.'
        )
        mail.send(msg)
        print('Email sent!')

# Calculate the time difference between the current time and 3:00 PM
now = datetime.now()
scheduled_time = datetime(now.year, now.month, now.day, 6,7)  # 3:00 PM
time_difference = scheduled_time - now

# If the scheduled time has already passed for today, schedule it for the same time tomorrow
if time_difference.total_seconds() < 0:
    scheduled_time += timedelta(days=1)

# Schedule the email to be sent at the calculated time
s.enterabs(scheduled_time.timestamp(), 1, send_email, ())

if __name__ == '__main__':
    # Run the scheduled tasks
    print('Scheduled tasks are running...')
    #s.run()
    app.run(debug=True)"""



    
 

    
 

    



"""from flask import Flask
from flask_mail import Mail, Message
import smtplib
import schedule
import time
import threading
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
mail = Mail(app)

# Flask app configuration for Gmail SMTP


# Flask app configuration for file upload
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

mail.init_app(app)


# Function to send email with PDF attachment
def send_email_with_attachment():
    try:
        with app.app_context():
            msg = Message('Scheduled Email with Attachment', sender='rutuja.myfirstplacement@gmail.com', recipients=['rutujabhoyate151@gmail.com'])
            msg.body = 'This is a one-time scheduled email with a PDF attachment.'
            
            # Attach the PDF file
            pdf_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'your_pdf_file.pdf')
            with app.open_resource(pdf_file_path) as pdf_file:
                msg.attach('your_pdf_file.pdf', 'application/pdf', pdf_file.read())

            mail.send(msg)
            print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print('Error sending email:', e)


# Schedule the email to be sent at a specific date and time
scheduled_time = "2023-12-14 17:18:00"  # Change this to your desired date and time

schedule_time_struct = time.strptime(scheduled_time, "%Y-%m-%d %H:%M:%S")
schedule_time_epoch = time.mktime(schedule_time_struct)

current_time_epoch = time.time()
time_difference_seconds = schedule_time_epoch - current_time_epoch

# Schedule the email to be sent after the time difference
schedule.every(time_difference_seconds).seconds.do(send_email_with_attachment)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
    if time.time() > schedule_time_epoch + 60:
        break

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)"""
    
    
'''from flask import Flask
from flask_mail import Mail, Message
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib

app = Flask(__name__)
mail = Mail(app)

# Flask app configuration for Gmail SMTP

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'rutuja.myfirstplacement@gmail.com'
app.config['MAIL_PASSWORD'] = 'ppvk mqvi erqm zsmh'
app.config['MAIL_DEFAULT_SENDER'] = 'rutuja.myfirstplacement@gmail.com'


mail.init_app(app)

# Function to send email
def send_email():
    try:
        with app.app_context():
            msg = Message('Scheduled Email', sender='rutuja.myfirstplacement@gmail.com', recipients=['rutujabhoyate1510@gmail.com'])
            msg.body = 'This is a scheduled email sent at 5:18 PM.'
            mail.send(msg)
            print('Email sent successfully!')
    except smtplib.SMTPException as e:
        print('Error sending email:', e)

# Create and configure scheduler
scheduler = BlockingScheduler()
scheduler.add_job(send_email, trigger='cron', minute=12, hour=18)

if __name__ == '__main__':
    scheduler.start()
    app.run(debug=True)'''
