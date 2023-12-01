# TODO: 1.스케줄링
#       2.리뷰 수집 중복체크(중복 X)
#       3.데이터베이스에 수집 된 데이터 → Excel 저장
#       4.데이터베이스에 수집 된 데이터 → 간단한 텍스트 분석
#       5.데이터베이스에 수집 된 데이터 → WordCloud 시각화
#  TIP: 이모티콘 → 어떤 형식? → 정규식(제거)

from collect.collect_daum_movie_review import review_collector
from db.movie_dao import get_last_review


def main():
    print("=" * 100)
    print("== 영화 리뷰 수집기 ver1.0 ==")
    print("=" * 100)
    movie_code = input("== 영화코드: ")  # 169328
    print('== MSG: "매일 낮 12시 수집"')

    # DB에서 데이터 조회 실패 → None
    last_date = get_last_review()
    if last_date == None:
        last_date = 0
    else:
        last_date = int(last_date["int_regdate"])

    # last_date = DB에 저장된 마지막 리뷰 날짜
    review_collector(movie_code, last_date)


if __name__ == "__main__":
    main()
