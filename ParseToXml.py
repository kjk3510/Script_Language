# -*- coding: utf-8 -*-


import urllib.request
from urllib.parse import quote
import xml.etree.ElementTree as ET
#import requests as rq
#import smtplib
#from email.mime.text import MIMEText
import os
import glob


class Data:
    SEARCH = 1
    SCHTOSAVE = 1
    SCHTOEM = 2

    SAVE = 2
    SVTOEM = 1

    EMAIL = 3
    EMTOSCH = 1

    PLUSDATA = 4
    PDTOSAVE = 1
    PDTOINFO = 1
    PDTOEM = 2

    Test_Name = None


    def __init__(self): # 파싱 등에 필요한 초기화 함수
        self.key = '47a1ee741e9545b1a868605931cbdd61'
        self.url = None
        self.sigunNm = None
        self.filename = None
        self.tree = None
        self.root = None


    def parse(self, Name): # 오픈api를 파싱하기위한 함수
        self.url = "http://openapi.gg.go.kr/Parmacy?KEY=%s&pSize=1000&SIGUN_NM=" % self.key + quote('%s' % self.sigunNm)
        data = urllib.request.urlopen(self.url).read()
        self.filename = "pharmacy" + ".xml"
        f = open(self.filename, "wb")
        f.write(data)
        f.close()
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()


    def printInfo(self, Name): # 파싱데이터 출력을 위한 함수
        for Parmacy in self.root.iter("Parmacy"):
            for row in Parmacy.iter("row"):
                print('--------------------------------------------------------------')
                print('시군코드\t\t:' + row.findtext('SIGUN_CD'))
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


    def save(self, Name): # 파싱데이터 저장을 위한 함수
        for Parmacy in self.root.iter("Parmacy"):
            for row in Parmacy.iter("row"):
                self.savename = "save.txt"
                fts = open(self.savename, "a")
                fts.write("--------------------------------------------------------------\n")
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
                fts.write("--------------------------------------------------------------\n")
                fts.write('\n')
            for head in Parmacy.iter("head"):
                fts.write('검색개수 : ' + head.findtext('list_total_count'))
                fts.close()
        print("데이터가 저장되었습니다.")

# 기존 데이터에 입려값 받아서 데이터 추가하기
    def plusdata(self, Name, SIGUN, BIZPLC, LOCPLC, LOCPLCROAD, BSN, LICENSG):
        for Parmacy in self.root.iter("Parmacy"):
            for row in Parmacy.iter("row"):
                self.savename = "save2.txt"
                fts = open(self.savename, "a")
                fts.write("--------------------------------------------------------------\n")
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
                fts.write("--------------------------------------------------------------\n")
                fts.write('\n')
                fts.close()
        fts = open(self.savename, "a")
        fts.write("--------------------------------------------------------------\n")
        fts.write('시군명\t\t\t:' + SIGUN)
        fts.write('\n')
        fts.write('약국이름\t\t:' + BIZPLC)
        fts.write('\n')
        fts.write('지번주소\t\t:' + LOCPLC)
        fts.write('\n')
        fts.write('도로명주소\t\t:' + LOCPLCROAD)
        fts.write('\n')
        fts.write('운영현황\t\t:' + BSN)
        fts.write('\n')
        fts.write('인허가구분명\t\t:' + LICENSG)
        fts.write('\n')
        fts.write("--------------------------------------------------------------\n")
        fts.write('\n')
        fts.close()

# 추가한 데이터값 출력하기
    def plusdataInfo(self, Name, SIGUN, BIZPLC, LOCPLC, LOCPLCROAD, BSN, LICENSG):
        fp = open("save2.txt", "r")
#        while True:
#            line = fp.readline()
#            if not line: break
#            print(line)
        rfp = fp.read() # 위에 코드로하면 한칸씩 띄어서 읽혀진다.
        print(rfp)
        fp.close()

# 기존에 파일이 있으면 삭제하기
    def delete(self):
        files = glob.glob("*")
        for f in files:
            if f == 'save.txt':
                os.remove(f)

# 기존에 파일이 있으면 삭제하기 2
    def deletep(self):
        files = glob.glob("*")
        for f in files:
            if f == 'save2.txt':
                os.remove(f)