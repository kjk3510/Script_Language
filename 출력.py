# -*- coding: utf-8 -*-

import smtplib
import os
import email.mime.multipart
from email import encoders
from email import utils
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

host='smtp.gmail.com' #Gmail smtp server address

port='587' #smtp port

#imagefile='logo.png'
textfile='save.txt'



sender='kjk3510@gmail.com' #sender email address

passward = 'dowkqh1313!'

recipient='kjk3510@naver.com' #recipient email address



# Create MIMEBase

msg=MIMEBase('multipart','mixed')

msg['Subject']='Test Email in html.logo'

msg['From']=sender

msg['To']=recipient




# Create MIMEImage

#imageF=open(imagefile,'rb')

#imagePart=MIMEImage(imageF.read())

#imageF.close()

# Create MIMEtxt

textF=open(textfile,'rb')

textPart=MIMEImage(textF.read())

textF.close()



# attach html,image

#msg.attach(imagePart)
msg.attach(textPart)



# mail send

s=smtplib.SMTP(host,port)

s.set_debuglevel(1) #debuging

s.ehlo()

s.starttls()

s.ehlo()

s.login(sender,passward)

s.sendmail(sender,[recipient],msg.as_string())

s.close()


