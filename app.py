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


"""@app.route('/')
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
    mail.send(msg)"""
    
def send_email(to, subject, body, cc=None, bcc=None, attachments=[]):
    msg = Message(subject, recipients=[to], body=body, cc=cc, bcc=bcc)

    for attachment in attachments:
        with app.open_resource(attachment) as attachment_file:
            msg.attach('output.pdf', 'application/pdf', attachment_file.read())

    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    


