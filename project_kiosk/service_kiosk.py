# 키오스크 기능들

# 사용자 메뉴 선택 기능!
#  1.메인메뉴 선택(1, 2, 3, 99)
#  2.세부메뉴 선택(1~4 or 1~3)
#    max_cnt : 메뉴별 갯수
#    menu_type : main or sub
def user_choice(max_cnt, menu_type):
    while True:
        choice = int(input(">> 번호: "))
        # main 메뉴에서 99를 입력하면 프로그램 종료!
        if choice == 99 and menu_type == "main":
            return choice
        # main or sub에서 메뉴 선택
        if max_cnt >= choice >= 1:
            return choice
        else:
            print("MSG: 올바른 번호를 입력하세요.")


# 메뉴 출력 기능!
def show_menu():
    pass