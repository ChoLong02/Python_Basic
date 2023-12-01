# 스케줄러(Scheduler)
#  - 정해진 일정에 맞춰서 프로그램을 동작!
#  예) 12시간에 한번씩
#      5분마다
#      특정일에만(크리스마스)

# 스케줄러 + 프로그램 → 완성 → 서버(동작)

# apscheduler
#  1.blocking
#   - 스케줄러 + 프로그래만 동작
#  2.background
#   - 동작은 하되 뒤에서 조용히!


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time

# print_today()를 호출하면 현재 시간 출력
def print_today():
    print(datetime.now())  # 현재시간 출력

def print_love():
    print("I Love You")


# 1.스케줄러 생성
scheduler = BlockingScheduler()

# 2.스케줄러 일 할당(일, 주기, 5초)
#  - date:      특정 날짜 및 시간에 1번만 동작
#  - interval:  주기별로(5초, 10분, 1시간)
#  - CRON(★):   만능(매일 언제~)
scheduler.add_job(print_today, "interval", seconds=5)
scheduler.add_job(print_love, "cron", hour="11", minute="29")

# 3.스케줄러 실행
scheduler.start()

# 임의의 Work
# while True:
#     time.sleep(1)