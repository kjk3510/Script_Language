# -*- coding: utf-8 -*-


import urllib.request
from urllib.parse import quote
import xml.etree.ElementTree as etree
import requests as rq
import smtplib
from email.mime.text import MIMEText



class Data:


    def __init__(self):
        self.key = '47a1ee741e9545b1a868605931cbdd61'
        self.url = None
        self.sigunNm = None
        self.filename = None
        self.tree = None
        self.root = None

    def parse(self, Name):
        self.url = "http://openapi.gg.go.kr/Parmacy?KEY=%s&pSize=1000&SIGUN_NM="%self.key + quote('%s'%self.sigunNm)
        data = urllib.request.urlopen(self.url).read()
        self.filename = "pharmacy" + ".xml"
        f = open(self.filename, "wb")
        f.write(data)
        f.close()
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()


    def printInfo(self, Name):
        for Parmacy in self.root.iter("Parmacy"):
            for row in Parmacy.iter("row"):
                print('--------------------------------------------------------------')
                print('시군명\t\t\t:' + row.findtext('SIGUN_NM'))
                print('약국이름\t\t:' + row.findtext('BIZPLC_NM'))
                print('지번주소\t\t:' + row.findtext('LOCPLC_LOTNO_ADDR'))
                print('도로명주소\t\t:' + row.findtext('LOCPLC_ROADNM_ADDR'))
                print('운영현황\t\t:' + row.findtext('BSN_STATE_NM'))
                print('인허가구분명\t:' + row.findtext('LICENSG_DIV_NM'))
                print('--------------------------------------------------------------')
                print('\n')
            for head in Parmacy.iter("head"):
                print('검색개수 : ' + head.findtext('list_total_count'))


    def save(self, Name):
        for Parmacy in self.root.iter("Parmacy"):
            for row in Parmacy.iter("row"):
                fts = open('save.txt', "a")
                fts.write("---------------------------------------------------------\n")
                fts.write('시군명\t\t\t:' + row.findtext('SIGUN_NM'))
                fts.write('\n')
                fts.write('약국이름\t\t:' + row.findtext('BIZPLC_NM'))
                fts.write('\n')
                fts.write('지번주소\t\t:' + row.findtext('LOCPLC_LOTNO_ADDR'))
                fts.write('\n')
                fts.write('도로명주소\t\t:' + row.findtext('LOCPLC_ROADNM_ADDR'))
                fts.write('\n')
                fts.write('운영현황\t\t:' + row.findtext('BSN_STATE_NM'))
                fts.write('\n')
                fts.write('인허가구분명\t\t:' + row.findtext('LICENSG_DIV_NM'))
                fts.write('\n')
                fts.write("---------------------------------------------------------\n")
                fts.write('\n')
            for head in Parmacy.iter("head"):
                fts.write('검색개수 : ' + head.findtext('list_total_count'))
                fts.close()

    def sendemail(self):
        smtpHost = "smtp.test.com"
        msq = MIMEText('save.txt')
        senderAddr = "kjk3510@naver.com"
        recipientAddr = "kjk3510@naver.com"
        msq['Subject'] = "test mail"
        msq['From'] = senderAddr
        msq['To'] = recipientAddr

        s = smtplib.SMTP(smtpHost)
        s.connect()
        s.sendmail(senderAddr,[recipientAddr],msq.as_string())
        s.close()