# -*- coding: utf-8 -*-


from ParseToXml import Data


def main():
    data = Data()

    while(1):
        menu = 0
        data.bicycledong = None
        data.rentnum = 0

        print("원하는 정보를 고르세요")
        print("1. 공공 공기주입기 위치")
        print("2. 공공 자전거편의시설 위치")

        while(menu < 1 or menu > 2):
            menu = int(input("번호입력 : "))
            print('\n\n')
        if menu == data.BICYCLE:
            data.bicycledong = str(input("동 입력 : "))



        elif menu == data.BICYRENT:
            data.rentnum = (input("동 입력 : "))

        data.parse(menu)
        data.printInfo(menu)
        print("\n")


if __name__ == "__main__":
    main()

