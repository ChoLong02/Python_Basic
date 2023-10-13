################################################
# "스타벅스" 카페 키오스트 프로그램
#   - 일자: 2023년10월13일
#   - 작성자: cholong02
#   - 내용: 카페 음료를 주문 및 판매하는 콘솔 프로그램

# 조건
#  1.사용자는 최대 음료 1개, 베이커리 1개, 굿즈1개 구매 가능!

from service_kiosk import user_choice

# 메뉴와 가격표
#  - Dict Type → 데이터베이스
main_name = {1: "음료(Drink)", 2: "빵(Bakery)", 3: "굿즈(Goods)"}

drink_name = {1: "아메리카노", 2: "돌체콜드브루", 3: "딸기라떼", 4: "자몽에이드"}
bakery_name = {1: "카스테라", 2: "크로플", 3: "바움쿠헨"}
goods_name = {1: "텀블러", 2: "비치타월", 3: "무드등"}

drink_price = {1: 3000, 2: 4500, 3: 6000, 4:5000}
bakery_price = {1: 4500, 2: 5000, 3: 7000}
goods_price = {1: 18000, 2: 7000, 3: 17000}

# 고객 주문 기록 저장
menu_save = []   # 고객 주문 메뉴 기록
price_save = []  # 고객 주문 금액 기록

# 1.메인 메뉴 출력
print("■" * 50)
print("■■ == 스타벅스 == ")
print("■■ == ver 1.2 ")
print("■■ 메인 메뉴")
for i in range(len(main_name)):
    print(f"■□   {i+1}.{main_name[i+1]}")
print("■" * 20)

# 2.메인 메뉴 선택
choice = user_choice(len(main_name), "main")


# 3.세부 메뉴 출력
if choice == 1:    # 음료
    print("▲▲ 음료(Drink) 메뉴")
    for i in range(len(drink_name)):
        print(f"▲△   {i+1}.{drink_name[i+1]}({drink_price[i+1]})")
    # 4.세부 메뉴 선택
    sub = user_choice(len(drink_name), "sub")
    # 5.음료 주문 저장
    menu_save.append(drink_name[sub])
    price_save.append(drink_price[sub])
elif choice == 2:  # 빵
    print("▲▲ 빵(Bakery) 메뉴")
    for i in range(len(bakery_name)):
        print(f"▲△   {i + 1}.{bakery_name[i + 1]}({bakery_price[i + 1]})")
    # 4.세부 메뉴 선택
    sub = user_choice(len(bakery_name), "sub")
    # 5.음료 주문 저장
    menu_save.append(bakery_name[sub])
    price_save.append(bakery_price[sub])
elif choice == 3:  # 굿즈
    print("▲▲ 굿즈(Goods) 메뉴")
    for i in range(len(goods_name)):
        print(f"▲△   {i + 1}.{goods_name[i + 1]}({goods_price[i + 1]})")
    # 4.세부 메뉴 선택
    sub = user_choice(len(goods_name), "sub")
    # 5.음료 주문 저장
    menu_save.append(goods_name[sub])
    price_save.append(goods_price[sub])
elif choice == 99:
    print("MSG: 스타벅스 키오스크를 종료합니다.")
    exit()

for menu in menu_save:
    print(menu)
for price in price_save:
    print(price)

