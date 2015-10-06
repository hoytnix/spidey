from core import yandex  as scrape_yandex
from core import weblogs as scrape_weblogs
from core import google  as scrape_google
from core import extract

from time import strftime
import sys

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def google():
    msg = "[%s] Google" % strftime("%H:%M:%S")
    print(msg)
    f = scrape_google()

    extract(f)

@sched.scheduled_job('interval', minutes=60)
def weblogs():
    msg = "[%s] Weblogs" % strftime("%H:%M:%S")
    print(msg)
    f = scrape_weblogs()

    extract(f)

@sched.scheduled_job('interval', minutes=10)
def yandex():
    msg = "[%s] Yandex" % strftime("%H:%M:%S")
    print(msg)
    f = scrape_yandex()
    
    extract(f)

if __name__ == "__main__":
    try:
        sched.start()        # start the scheduler
    except KeyboardInterrupt:
        print("\nbye!")
        sys.exit(0)