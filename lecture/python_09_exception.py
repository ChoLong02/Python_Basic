# 예외 처리
#  ** 예외(Exception)
#   - 프로그램을 개발하면서 예상하지 못한 상황
#     ex) 사용자의 입력 오류
#   - 예외처리를 사용하면 프로그램이 종료되지 않음
#     프로그램 -> 입력 오류 -> 프로그램 종료(Error)
#     프로그램 -> 입력 오류 -> 예외 처리 -> 프로그램 종료 X
#   - 데이터베이스 또는 파일시스템 사용할 때는 반드시 예외처리!!

#  ** 예외 종류
#   1. 예측 가능한 예외
#     - 발생 여부를 개발자가 사전에 인지 가능 -> 예외 처리
#   2. 예측 불가능한 예외
#     - 서버에서 데이터 받기(서버 화재 발생으로 서버 종료)
#     ex) 스마트폰(카카오톡) -> 00친구와 톡방 -> 카카오 서버 접근 -> 데이터 전달 -> 스마트폰 출력

#  ** 예외 기본문법
# try:
#   예외 발생 가능 코드
# except 예외 타입:
#   예외 발생시 실행되는 코드
# else:
#   예외가 발생하지 않았을 때 실행되는 코드
# finally:
#   예외에 상관없이 무조건 실행(자원 해제)

# 가정: 수강신청 -> 종합정보시스템(조대 서버): 최대 2000명 동시접속
#  - 학생1 컴퓨터 -> 수강신청 -> 종합정보시스템(Connect)
#    수강신청 완료 -> 자원해제(Connect 끊기)

# 정상실행: try -> else -> finally
# 예외실행: try -> except -> finally
# * else, finally 생략 가능
# * try~except 한 쌍

from urllib.request import urlopen, HTTPError

try:
    html = urlopen("http://www.naver.commmmm")
except HTTPError as e:
    print(e)
else:
    print("no error")
finally:
    print("자원해제")

