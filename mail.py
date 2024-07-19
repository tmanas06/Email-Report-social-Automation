from email.message import EmailMessage
import ssl
import smtplib
import configparser
from app import app

config = configparser.ConfigParser()
config.read('C:\\Users\\tmana\\OneDrive\\Desktop\\analytics\\working\\Social_report\\Email-social-report_automatically\\config.ini') # config file path
             
sender_email = 'you@gmail.com'
receiver_email = ['to@gmail.com', 'to@gmail.com'] # you can add as many gmail as you want
password = config['mails']['password']  # Use the 16 digit password from the google account setting


def send_report_via_email(report_html):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_email)
    msg['Subject'] = "Report"
    msg.set_content(report_html, subtype='html')
    
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    with app.test_client() as c:
        response = c.get('/')
        report_html = response.get_data(as_text=True)
        send_report_via_email(report_html)
