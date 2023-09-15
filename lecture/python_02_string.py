# 문자열의 이해(String)

# 1.문자열 인덱스
#  - 문자열은 각 문자마다 순서(인덱스)가 있음
#  - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
#  - 인덱스 시작은 0
#  - 인덱스는 공백 포함
print("="*100)
print("python")

# 2.문자 추출
#  - 인덱스를 통해서 문자 추출
#  - 인덱스 범위 벗어난 경우 오류(Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9]) Error

# -1 인덱스(Reverse Index)
#  - 우측에서 좌측으로 인덱스
#  - 시작값 -1
print(lang[-1])
print(lang[-3])

# ID를 Email: cherry1024@gmail.com
#  - 로그인: cherry1024@gmail.com님

# 3.문자열 슬라이싱
#  - lang[3]: 문자 1개만 추출
#  - 부분 문자열을 추출하고 싶은 경우
#  - 시작인덱스, 끝인덱스 필요!
msg = "Python is all you need"
print(msg[0:6])  # 끝 인덱스+1
print(msg[:6])  # 시작 인덱스 생략 -> 자동 0 입력
print(msg[3:])  # 끝 인덱스 생략 -> 자동 -1 입력

# Quiz
# msg에서 "need"만 추출
# 정방향 인덱스 ->
# 역방향 인덱스 -> 
