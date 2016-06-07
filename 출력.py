# -*- coding: utf-8 -*-


import urllib.request
from urllib.parse  import quote
import xml.etree.ElementTree as etree



class Data:
    DATEINFO = 1

    def __init__(self):
        self.key = '4649626c536b6a6b3130317146447052'
        self.num = None
        self.filename = None
        self.url = None
        self.tree = None
        self.root = None

    def parse(self, menu):
        self.select_menu = menu
        if self.select_menu == self.DATEINFO:
            self.url = "http://openapi.seoul.go.kr:8088/%s/xml/BicyclePumpInfo/1/5/%d" % (self.key, self.num)
            data = urllib.request.urlopen(self.url).read()
            self.filename = self.num + ".xml"
        f = open(self.filename, "wb")
        f.write(data)
        f.close()
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()
            
    def printInfo(self, menu):
        self.select_menu = menu
        if self.select_menu == self.DATEINFO:
            for boxOfficeResult in self.root.iter("boxOfficeResult"):
                for dailyBoxOffice in boxOfficeResult.iter("dailyBoxOffice"):
                    print('--------------------------------------------------------------')
                    print('설치지점명\t\t:' + dailyBoxOffice.findtext('SET_LOC'))
                    print('설치장소\t\t:' + dailyBoxOffice.findtext('SET_PLACE'))
                    print('위치\t\t:' + dailyBoxOffice.findtext('LOCATION'))
                    print('개소\t:' + dailyBoxOffice.findtext('SPOT'))
                    print('대수(대)\t\t:' + dailyBoxOffice.findtext('EA_COUNT'))
                    print('--------------------------------------------------------------')
            



