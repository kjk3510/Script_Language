# -*- coding: utf-8 -*-


from ParseToXml import Data # 파싱데이터를 받아오기위함
from sendtomail import send_mail # 이메일보내기 위함


def main():
    data = Data()

    while(1):
        menu = 0
        sc_menu = 0
        sv_menu = 0
        em_menu = 0
        pl_menu = 0
        pls_menu = 0
        data.sigunNm = None
        Name = None
        SIGUN = None
        BIZPLC = None
        LOCPLC = None
        LOCPLCROAD = None
        BSN = None
        LICENSG = None

        print("원하시는 작업을 고르세요."'\n')
        print("1. 출력하기"'\n')
        print("2. 저장하기"'\n')
        print("3. 메일보내기"'\n')
        print("4. 정보추가하기"'\n')
        print("5. 지도띄우기"'\n')

        while(menu < 1 or menu > 4):
            menu = int(input("번호를 입력하세요 : "))
            print('\n\n')

        if menu == data.SEARCH: # 파싱데이터 출력하기
            data.sigunNm = str(input("시군명을 입력하세요 : "))
            Name = data.sigunNm
            data.parse(Name)
            data.printInfo(Name)
            print('\n')
            print("1. 출력값 저장하기"'\n')
            print("2. 출력값 전송하기"'\n')
            while(sc_menu < 1 or sc_menu > 2):
                sc_menu = int(input("번호를 입력하세요 : "))
                print('\n\n')
            if sc_menu == data.SCHTOSAVE:
                data.delete()
                data.save(Name)

            elif sc_menu == data.SCHTOEM:
                data.delete()
                data.save(Name)
                user_id = str(input("이메일입력 : "))
                send_mail("kjk3510@gmail.com", user_id, Name + " 약국정보", "test to email", "save.txt")

        elif menu == data.SAVE: # 파싱데이터 저장하기
            data.sigunNm = str(input("시군명을 입력하세요 : "))
            Name = data.sigunNm
            data.parse(Name)
            data.delete()
            data.save(Name)
            print('\n')
            print("이메일전송 원하면 1번을 입력하세요 : "'\n')
            sv_menu = int(input("번호 입력 : "))
            if sv_menu == data.SVTOEM:
                user_id = str(input("이메일입력 : "))
                send_mail("kjk3510@gmail.com", user_id, Name + " 약국정보", "test to email", "save.txt")

        elif menu == data.EMAIL: # 파싱데이터 이메일보내기
            data.sigunNm = str(input("시군명을 입력하세요 : "))
            Name = data.sigunNm
            data.parse(Name)
            data.delete()
            data.save(Name)
            print('\n')
            user_id = str(input("이메일입력 : "))
            send_mail("kjk3510@gmail.com", user_id, Name + " 약국정보", "test to email", "save.txt")
            print('\n')
            print("출력하기 원하면 1번을 입력하세요"'\n')
            em_menu = int(input("번호 입력 : "))
            if em_menu == data.EMTOSCH:
                data.printInfo(Name)

        elif menu == data.PLUSDATA: # 파싱데이터에 추가하기 ------ 수정필요 예제로 연습중
            data.sigunNm = str(input("시군명을 입력하세요 : "))
            Name = data.sigunNm
            data.parse(Name)
            print('\n')
            print("추가데이터를 입력하려면 1을 입력하세요"'\n')
            pl_menu = int(input("번호를 입력하세요 : "))
            if pl_menu == data.PDTOSAVE:
                SIGUN = str(input("추가할 시군명 : "))
                BIZPLC = str(input("추가할 약국이름 : "))
                LOCPLC = str(input("추가할 지번주소 : "))
                LOCPLCROAD = str(input("추가할 도로명주소 : "))
                BSN = str(input("추가할 운영현황 : "))
                LICENSG = str(input("추가할 인허가구 : "))
                data.deletep()
                data.plusdata(Name, SIGUN, BIZPLC, LOCPLC, LOCPLCROAD, BSN, LICENSG)
                print('\n')
                print("1. 추가데이터 출력하기"'\n')
                print("2. 추가데이터 전송하기"'\n')
                while(pls_menu < 1 or pls_menu > 2):
                    pls_menu = int(input("번호를 입력하세요 : "))
                if pls_menu == data.PDTOINFO:
                    data.plusdataInfo(Name, SIGUN, BIZPLC, LOCPLC, LOCPLCROAD, BSN, LICENSG)
                elif pls_menu == data.PDTOEM:
                    user_id = str(input("이메일입력 : "))
                    send_mail("kjk3510@gmail.com", user_id, Name + " 약국정보 + 데이터추가", "test to email", "save2.txt")




#        elif menu == data.SAVE:



#        data.parse(Name)
#        data.printInfo(Name)
#        data.save(Name)
#        send_mail("kjk3510@gmail.com", "kjk3510@naver.com", "test", "test to email", "save.txt")
        print("\n")


if __name__ == "__main__":
    main()

