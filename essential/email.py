
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from os import environ

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login(environ.get("EMAIL"),environ.get("EMAIL_PASSWORD"))

def message(subject,text):
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg.attach(MIMEText(text,"html"))
	return msg

def send_email(email,subject,text):
    try:
        msg = message(subject, text)
        smtp.sendmail(from_addr=environ.get("EMAIL"),
            to_addrs=email, msg=msg.as_string())
        return True
    except Exception as e:
        print(e)
        return False

