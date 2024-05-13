import time
import datetime


while True:
    _now = datetime.datetime.now()
    print(_now.strftime("%H:%M:%S"))
    time.sleep(1)