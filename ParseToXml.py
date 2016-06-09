# -*- coding: utf-8 -*-


import urllib.request
from urllib.parse  import quote
import xml.etree.ElementTree as etree



class Data:
    MENUSELECT = 0
    BICYPUMP = 1
    BICYRENT = 2

    def __init__(self):
        self.pumpkey = '4649626c536b6a6b3130317146447052'
        self.rentkey = '5351664f416b6a6b35396967654e70'
        self.pumpnum = 0
        self.rentnum = 0
        self.filename = None
        self.pumpurl = None
        self.rentrul = None
        self.tree = None
        self.root = None

    def parse(self, menu):
        self.choose_num = menu
        if self.choose_num == self.BICYPUMP:
            self.pumpurl = "http://openapi.seoul.go.kr:8088/%s/xml/BicyclePumpInfo/1/%d" % (self.pumpkey, self.pumpnum)
            data = urllib.request.urlopen(self.pumpurl).read()
            self.filename = "BicyclePumpInfo" + ".xml"
        elif self.choose_num == self.BICYRENT:
            self.renturl = "http://openAPI.seoul.go.kr:8088/%s/xml/GeoInfoBikeConvenientFacilities/1/5/%d" % (self.rentkey, self.rentnum)
            data = urllib.request.urlopen(self.renturl).read()
            self.filename = "BicycleRentInfo" + ".xml"
        f = open(self.filename, "wb")
        f.write(data)
        f.close()
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()
            
    def printInfo(self, menu):
        self.choose_num = menu
        if self.choose_num == self.BICYPUMP:
            for BicyclePump in self.root.iter("BicyclePumpInfo"):
                for BicyclePumpInfo in self.root.iter("row"):
                    print('--------------------------------------------------------------')
                    print('설치지점명\t\t:' + BicyclePumpInfo.findtext('SET_LOC'))
                    print('설치장소\t\t:' + BicyclePumpInfo.findtext('SET_PLACE'))
                    print('위치\t\t\t:' + BicyclePumpInfo.findtext('LOCATION'))
                    print('개소\t\t\t:' + BicyclePumpInfo.findtext('SPOT'))
                    print('대수(대)\t\t:' + BicyclePumpInfo.findtext('EA_COUNT'))
                    print('주입방식\t\t:' + BicyclePumpInfo.findtext('PUMP_TYPE'))
                    print('결제정보\t\t:' + BicyclePumpInfo.findtext('PAYMENT'))
                    print('운영방식\t\t:' + BicyclePumpInfo.findtext('OPERATE_TYPE'))
                    print('--------------------------------------------------------------')
        elif self.choose_num == self.BICYRENT:
            for BicycleRent in self.root.iter("GeoInfoBikeConvenientFacilities"):
                for GeoInfoBikeConvenientFacilities in self.root.iter("row"):
                    print('--------------------------------------------------------------')
                    print('편의시설종류\t:' + GeoInfoBikeConvenientFacilities.findtext('CLASS'))
                    print('위치\t\t\t:' + GeoInfoBikeConvenientFacilities.findtext('ADDRESS'))
                    print('x좌표\t\t\t:' + GeoInfoBikeConvenientFacilities.findtext('X'))
                    print('y좌표\t\t\t:' + GeoInfoBikeConvenientFacilities.findtext('Y'))
                    print('--------------------------------------------------------------')