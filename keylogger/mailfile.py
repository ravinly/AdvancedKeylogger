from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import email 
import smtplib
import os
import sys
email_address="rithashetty19@gmail.com"
password="wkciixxpsaafubgg"
toaddr="1ds20cs220@dsce.edu.in"
def send_email(filename,attachment,toaddr):
    fromaddr=email_address
    msg=MIMEMultipart()
    msg['From'] = fromaddr
    msg['To']=toaddr
    msg['Subject']= "Log File"
    body="Body_of_the_mail"
    msg.attach(MIMEText(body,'plain'))
    filename=filename
    attachment=open(os.path.abspath("demo.txt"),'rb')
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    email.encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment: filename=%s"% filename)
    msg.attach(p)

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr,password)
    text=msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()


