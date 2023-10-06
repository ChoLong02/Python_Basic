# 함수(method, function)
#  - 어떤 일을 수행하는 코드 묶음
#  - 반복적으로 동작해야하는 일들!

# ex) 아침마다 보고서를 만들려면 15줄에 코드를 작성하고 실행
#     → 매일 아침마다 15줄 코드를 작성 및 실행(비효율적)
#     => 15줄 코드를 함수로 정의하고 함수를 실행(효율적)

# 함수 개발 가이드라인
#  1.함수 이름
#    + 함수 내용은 가능하면 짧게 작성(line 줄이기)
#    + 함수 이름에 함수의 역할과 의도를 명확히 드러낼 것!
#  ex) def print_hello():
#         print("Hello")

#  2.함수의 역할
#    + 하나의 함수에는 유사한 역할을 하는 코드만 포함
#    + 함수는 한 가지 기능만 명확히 정의
#  ex) def add_value(x, y):
#         return x+y

#  3.함수를 만들어야 하는 경우
#    + 공통적으로 사용되는 코드는 함수로 생성
#    + 복잡한 로직이 사용되는 경우 식별 가능한 이름의 함수로 생성

# 함수의 종류
#  1.내장함수(Built-in function)
#    + python에서 내부적으로 제공하는 함수
#    ex) print(), len(), type(), format(), list(), tuple()

#  2.외장함수(library or module)
#    + 라이브러리: 다른 사람이 만든 코드 묶음
#    + import문을 통해서 라이브러리 모듈을 제공
#    ex) import pandas as pd
#        df_data = pd.read_excel("path...")

#  3.사용자 정의 함수
#    + 개발자가 직접 만들어서 사용하는 함수

# 함수 이름 규칙
#  Naming Rule => snake_case

# 함수 정의
#  1.기본 함수 문법
# def 함수명(parameter1, parameter2, ...):
#     실행문
#     return 반환값

#  2.함수 정의시 "def" 키워드 사용(define)
#  3.인자(argument or parameter) 정의: 함수 입력 값
#  4.return: 함수 종료 의미
#  5.return 반환값: 함수 종료 + 호출문으로 반환값 전달(tuple)
#  6.return 생략가능 -> 들여쓰기 종료되면 함수 종료
#  7.parameter와 return은 사용하지 않을수도 있음
#    (입력과 반환이 없는 함수도 존재)
