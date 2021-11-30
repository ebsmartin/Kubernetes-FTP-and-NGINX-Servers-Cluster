import smtplib
from pathlib import Path
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import subprocess
import time

SMTP_SERVER = 'smtp.gmail.com' # email server
SMTP_PORT = 587 # email server port
GMAIL_USERNAME = 'hogwartscluster@gmail.com'
GMAIL_PASSWORD = 'qPyD&DiJ?b?@D&5'

def send_mail(to_address, subject, body, file_path):
  msg = MIMEMultipart() # create MIME object for entire email
  msg['From'] = GMAIL_USERNAME
  msg['To'] = to_address
  msg['Subject'] = subject
  msg.attach(MIMEText(body))  # attach email content

  attachment = MIMEBase('application', "octet-stream")  # create MIME object for file attachment
  attachment.set_payload(open(file_path, "rb").read())
  encoders.encode_base64(attachment)
  attachment.add_header('Content-Disposition', f'attachment; filename={Path(file_path).name}')
  msg.attach(attachment)  # attach file attachment MIME object
  
  mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) # connect to mail server
  mail.starttls() # use tls encryption
  mail.login(GMAIL_USERNAME, GMAIL_PASSWORD)
  mail.sendmail(GMAIL_USERNAME, to_address.split(","), msg.as_string())
  mail.quit()

def main(): # called in Hogwarts_Security_Protocol.py
  # declare email variables
  send_to = 'emartin.exe@gmail.com, victorberggren3@gmail.com'  # blakedavis12302@gmail.com,
  subject = 'Hogwarts Cluster Accelerometer Activated'
  body = 'The accelerometer sensor was activated at: ' + time.ctime()
  subprocess.call('./auth_logs.sh')
  attachment = 'auth_logs.txt'
  send_mail(send_to, subject, body, attachment)

if __name__ == "__main__":
  main()