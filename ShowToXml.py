# -*- coding: utf-8 -*-


from ParseToXml import Data


def main():
    data = Data()
    sigunNm = None

    while(1):
        print("시군을 입력하세요"'\n')

        if sigunNm == None:
            data.sigunNm = str(input("시군명 : "))
            Name = data.sigunNm
            print('\n\n')

        data.parse(Name)
        data.printInfo(Name)
        print("\n")


if __name__ == "__main__":
    main()

