#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email import encoders
from email import utils
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# 메일 보내기위한 기본 정보를 입력

smtp_server  = "smtp.gmail.com"
port ='587'
userid = "kjk3510@gmail.com"
passwd = "dowkqh1313!"

# 메일을 보내기위한 함수 작성

def send_mail(from_user, to_user, subject, text, attach):
        COMMASPACE = ", "
        msg = MIMEMultipart("alternative")
        msg["From"] = from_user
        msg["To"] = to_user
        msg["Subject"] = Header(s=subject, charset="utf-8")
        msg.attach(MIMEText(text, "txt", _charset="utf-8"))
        if (attach != None):
                part = MIMEBase("application", "octet-stream")
                part.set_payload(open(attach, "rb").read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % os.path.basename(attach))
                msg.attach(part)

        smtp = smtplib.SMTP(smtp_server, port)
        smtp.set_debuglevel(1) #debuging
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(userid, passwd)
        smtp.sendmail(from_user, to_user, msg.as_string())
        smtp.close()