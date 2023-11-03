# WebCrawling(웹 크롤링)
#  - 웹 페이지에서 원하는 데이터를 수집하는 기술
#  - 데이터가 필요한 작업 → 원하는 데이터가 없는 경우!
#                           (제공X, 다운X)
#    → 웹크롤링을 사용해서 직접 데이터를 수집

#  - 직업: 웹 크롤러(전문),
#  -       데이터엔지니어(웹크롤링 + @)
#  - 웹크롤링 + 스케줄링 -> 자동화

# 외부 라이브러리(다운로드 + import)
#  1.BeautifulSoup4(bs4)
#  2.Requests
#  3.Selenium

#  웹 페이지
#    - 정적 페이지(Requests + bs4)
#    - 동적 페이지(Selenium + bs4)

# Anaconda Prompt
#  > conda env list -> basic 확인
#  > 없으면: conda create -n basic python=3.8
#  > conda activate basic
#  > pip install requests
#  > pip install beautifulsoup4
#  > pip install selenium
# import requests
# import selenium
# from bs4 import BeautifulSoup

# 웹 프로그래밍 기초(속성)
#  - 프론트 엔드: 사용자 화면 개발
#  - 백 엔드: 서비스와 DB 개발
#  - 풀 스택: 프론트 엔드 + 백 엔드

# MVC 패턴
#  - VIEW(사용자 화면)
#  - CONTROLLER
#  - MODEL(데이터베이스:저장)

# 웹 페이지 화면 구현
#  - 웹 표준: HTML, CSS, Javascript
#  1.HTML: 프레임 구현
#  2.CSS: 디자인(색상, 크기, 모양, 등등)
#  3.Javascript: 동적 기능

# HTML 속성
#  - <tag></tag> 구현
#  - tag 종류: div, span, a, h4, etc...
#  - tag 종속관계
#    <div>
#      <span>
#        <span></span>
#      </span>
#      <span></span>
#    </div>
#    div: 부모
#     ㄴ span: 자식
#    종속관계: 부모자식 (div > span: div태그의 자식 태그인 span)
#              자손(div span: div태그 안에 있는 모든 span)

#  선택자
#   1.ID(#): 유일한 선택자
#   2.CLASS(.): 복수 선택자

import requests
from bs4 import BeautifulSoup
url = "https://v.daum.net/v/20231101111111618"  # 수집하고 싶은 웹사이트 주소

# 1.URL에 접속해서 전체 소스코드 가져오기!
result = requests.get(url)
# status_code: 200(성공)
#              400번대, 500번대 오류
# print(result)
# print(result.text)

# 2.전체소스코드(requests) → bs4
doc = BeautifulSoup(result.text, "html.parser")

# 3.원하는 정보 수집
reg_date = doc.select("span.num_date")[0].get_text()
print(f"날짜: {reg_date}")

title = doc.select("h3.tit_view")[0].get_text()
# select() → 결과: List Type
print(f"제목: {title}")

# 경고: Tag 이름으로는 절대 수집 X
content_list = doc.select("div.article_view p")
# content_list = ["<p>본문1</p>", "<p>본문2</p>",
#                 "<p>본문3</p>", "<p>본문4</p>", ...]

content = ""
# ex) p = "<p>본문1</p>"
for p in content_list:       #        content = content + p.get_text()
    content += p.get_text()  # 반복1: content = "" + "본문1"
print(f"본문: {content}")    # 반복2: content = "본문1" + "본문2"
                             # 반복2: content = "본문1본문2" + "본문3"


