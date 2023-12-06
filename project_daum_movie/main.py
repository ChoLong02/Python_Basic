# TODO:
#       3.데이터베이스에 수집 된 데이터 → Excel 저장
#       4.데이터베이스에 수집 된 데이터 → 간단한 텍스트 분석
#       5.데이터베이스에 수집 된 데이터 → WordCloud 시각화
#  TIP: 이모티콘 → 어떤 형식? → 정규식(제거)

from collect.collect_daum_movie_review import review_collector
from apscheduler.schedulers.blocking import BlockingScheduler


def main():
    print("=" * 100)
    print("== 영화 리뷰 수집기 ver1.0 ==")
    print("=" * 100)
    movie_code = input("== 영화코드: ")  # 169328
    print('== MSG: "매일 낮 12시 수집"')
    scheduler = BlockingScheduler()
    scheduler.add_job(review_collector,   # Job
                      trigger="cron",     # "Cron" 표기법 사용
                      args=[movie_code],  # Job의 매개변수
                      hour="12",          # 시간
                      minute="0")         # 분
    scheduler.start()


if __name__ == "__main__":
    main()
