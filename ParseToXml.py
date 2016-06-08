# -*- coding: utf-8 -*-

import os
import urllib.request
from urllib.parse  import quote
import xml.etree.ElementTree as etree
from xml.etree.ElementTree import *



class Data:

    def __init__(self):
        self.filelocation = None
        self.LOCATION = None
        self.tree = None
        self.root = None

    def parse(self):
        self.filelocation = open('C:\\Users\\Administrator\\Documents\\GitHub\\Script_Term_Project\\Script_Language\\test2.xml', 'r')
        self.tree = etree.parse(self.filelocation)
        self.root = self.tree.getroot()
            
    def printInfo(self):
        for BicyclePump in self.root.iter("root"):
            for root in self.root.iter("BicyclePumpInfo"):
                print('--------------------------------------------------------------')
                print('설치지점명\t\t:' + root.findtext('SET_LOC'))
                print('설치장소\t\t:' + root.findtext('SET_PLACE'))
                print('위치\t\t\t:' + root.findtext('LOCATION'))
                print('개소\t\t\t:' + root.findtext('SPOT'))
                print('대수(대)\t\t:' + root.findtext('EA_COUNT'))
                print('주입방식\t\t:' + root.findtext('PUMP_TYPE'))
                print('결제정보\t\t:' + root.findtext('PAYMENT'))
                print('운영방식\t\t:' + root.findtext('OPERATE_TYPE'))
                print('--------------------------------------------------------------')
            



