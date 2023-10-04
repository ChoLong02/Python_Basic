# 문제1) 입력 된 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i}={dan*i}")


# 문제2) 2단부터 9단까지 출력하는 코드
# 2x1=2
# 2x2=4
# ...
# 2x9=18
# 3x1=3
# ...
# 9x9=81

# 2단 => 1~9
# 3단 => 1~9
# 4단
# 5단
# ...
# 9단
for i in range(2, 10):  # 2~9단(i)
    for j in range(1, 10):  # 단 내에서 1~9
        print(f"{i}x{j}={i*j}")

# 문제3) list a의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# total => 총합
total = 0
for num in a:
   total += num  # total = total + num
length = len(a)
result = total / length
# round(값, 소수점숫자) : 반올림
print(round(result, 2))  # 평균값

# 문제4) list b에서 최소값 찾기!
b = [22, 1, 4, 7, 98]

print(num_min)  # 1 출력