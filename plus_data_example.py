# -*- coding: utf-8 -*-


from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse


list1 = []
list2 = []
list3 = []


#pf = open("plus_test.xml", "a")

note = Element("row")
#note.attrib["date"] = "20120104"

#to = Element("to")
#to.text = "Tove"
#note.append(to)

#SubElement(note, "SIGUN_CD").text = "123456"
SubElement(note, "SIGUN_NM").text = "시흥시"
SubElement(note, "BIZPLC_NM").text = "테스트 약국"
SubElement(note, "LOCPLC_LOTNO_ADDR").text = "시흥시 정왕동"
SubElement(note, "LOCPLC_ROADNM_ADDR").text = "시흥시 정왕로"
#SubElement(note, "LICENSG_DE").text = "20160613"
SubElement(note, "BSN_STATE_NM").text = "테스트중"
#SubElement(note, "CLSBIZ_DE").text = " "
#SubElement(note, "SUSPNBIZ_BEGIN_DE").text = " "
#SubElement(note, "SUSPNBIZ_END_DE").text = " "
#SubElement(note, "REOPENBIZ_DE").text = " "
#SubElement(note, "LOCPLC_AR").text = " "
#SubElement(note, "LOCPLC_ZIP_CD").text = "123456"
#SubElement(note, "PARMACY_BSN_AR").text = "1313"
SubElement(note, "LICENSG_DIV_NM").text = "약국"
#SubElement(note, "APPONT_DE").text = "20160613"
#SubElement(note, "WGS84_LOGT").text = "126.000000"
#SubElement(note, "WGS84_LAT").text = "37.000000"

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)
dump(note)

ElementTree(note).write("testtoplus.xml")

def plusplus():
    f = open('testtoplus.xml', 'r')
    ff = open("pharmacy.xml", "r", encoding='utf-8')
    fff = open("plus.xml", 'w')

    while True:
        line = f.readline()
        list1.append(line)
        if not line: break

    while True:
        line2 = ff.readline()
        list2.append(line2)
        if not line2: break

    list3 = list2 + list1


    fff.writelines(list3)

    f.close()
    ff.close()
    fff.close()

plusplus()
tree = parse("plus.xml")
root = tree.getroot()
Name = '시흥시'

def printInfo(self, Name): # 파싱데이터 출력을 위한 함수
    for row in root.iter("row"):
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

printInfo(Name)