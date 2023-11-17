from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import re
import math
from bs4 import BeautifulSoup
# pip install webdriver_manager
# pip install selenium

# Selenium + BeautifulSoup4
#  - Selenium: 전체소스코드 가져오기(+동적으로 페이지 조작)
#  - BeautifulSoup4: 필요한 데이터만 Select

# **Selenium
#   - 웹브라우저 검사(Test) 도구 → 데이터 수집
#   - 전용 브라우저(크롬, 파이어폭스, 등등)로 동작
#   - 전용 브라우저 Open → 작업 → 브라우저 Close(Default)

# ** Selenium 사용방법 2가지
#  1.직접 다운로드(크롬 브라우저)해서 사용
#    url: https://sites.google.com/chromium.org/driver/

#  2.실시간 다운로드 후 사용
options = Options()
# Selenium이 작업 완료 후에 전용 브라우저 종료 X
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=165591"
driver.get(url)
time.sleep(2)

# 페이지 소스 가져오기
doc_html = driver.page_source

doc = BeautifulSoup(doc_html, "html.parser")

# 영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print(movie_title)



total_review_cnt = doc.select("span.txt_netizen")[0].get_text()
# (187명) 에서 숫자만 추출 방법
#   1.문자열 슬라이싱 방법
# print(total_review_cnt[1:-2])
#   2.정규식 사용한 방법
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))

# 187 = 최초(10), 버튼1개(30개)
click_cnt = math.ceil((num_review - 10) / 30)

for i in range(click_cnt):
    # "평점 더보기" 버튼 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(2)

# 전체 소스코드 가져오기2(평점 모두 출력)
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")

print(len(review_list))

for item in review_list:
    print("=" * 100)
    review_score = item.select("")
    print(f"  - 평점: {review_score}")
    # review_content = item.select("")
    # print(f"  - 리뷰: {review_content}")
    # review_writer = item.select("")
    # print(f"  - 작성자: {review_writer}")
