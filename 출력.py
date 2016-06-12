# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

host='smtp.gmail.com' #Gmail smtp server address

port='587' #smtp port

imagefile='logo.png'



sender='kjk3510@gmail.com' #sender email address

recipient='kjk3510@naver.com' #recipient email address



# Create MIMEBase

msg=MIMEBase('multipart','mixed')

msg['Subject']='Test Email in html.logo'

msg['From']=sender

msg['To']=recipient




# Create MIMEImage

imageF=open(imagefile,'rb')

imagePart=MIMEImage(imageF.read())

imageF.close()



# attach html,image

msg.attach(imagePart)



# mail send

s=smtplib.SMTP(host,port)

s.set_debuglevel(1) #debuging

s.ehlo()

s.starttls()

s.ehlo()

s.login(sender,'dowkqh1313!')

s.sendmail(sender,[recipient],msg.as_string())

s.close()


