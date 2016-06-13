# -*- coding: utf-8 -*-


from ParseToXml import Data # 파싱데이터를 받아오기위함
from sendtomail import send_mail # 이메일보내기 위함
from plus_data_example import plusplus # 파싱데이터에 추가입력 하기위함


def main():
    data = Data()

    while(1):
        menu = 0
        sc_menu = 0
        sv_menu = 0
        em_menu = 0
        pl_menu = 0
        data.sigunNm = None
        Name = None

        print("원하시는 작업을 고르세요."'\n')
        print("1. 출력하기"'\n')
        print("2. 저장하기"'\n')
        print("3. 메일보내기"'\n')
        print("4. 정보추가하기"'\n')

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
            pl_menu = int(input("번호 입력 : "))
            if pl_menu == data.PDTOSAVE:
                plusplus()
                data.printInfo(Name)


#        elif menu == data.SAVE:



#        data.parse(Name)
#        data.printInfo(Name)
#        data.save(Name)
#        send_mail("kjk3510@gmail.com", "kjk3510@naver.com", "test", "test to email", "save.txt")
        print("\n")


if __name__ == "__main__":
    main()

