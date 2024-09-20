#!/Users/etn/Programming/py-venv/bin/python3
# or #!/usr/bin/env python3

import time
from newProvider import sch, cycleDay, pl2 # Bad code, fix later
import datetime as dt


# import newconfig as config

cycleDayStr = str(cycleDay)


summary = "["

for i in sch.periodList:
    try:
        summary += i["periodSymbol"];
    except KeyError:
        pass

summary += "]"

summary2 = "» ["

for i in pl2:
    try:
        summary2 += i["periodSymbol"];
    except KeyError:
        pass

summary2 += "]"


while True:
    classHasStarted = sch.updatePeriod()
    if classHasStarted:
        timeLeft = sch.getPeriodTimeLeft()
        try:
            if timeLeft >= dt.timedelta(0):
                print(summary, sch.getPeriodName(), sch.getPeriodSymbol(), str(timeLeft))
                time.sleep(20)
            else:
                print(summary, sch.getPeriodSymbol(), sch.getPeriodName(lookahead=1), sch.getPeriodSymbol(lookahead=1), str(sch.getPeriodTimeTil(lookahead=1)))
                time.sleep(1)
        except:
            print(summary, summary2)
            break
    else:
        print(summary, "Wait → " + sch.getPeriodName() + " " + sch.getPeriodSymbol() + " " + str(sch.getPeriodTimeTil()))
    timeToWait = (1000000 - sch.currentDatetime.microsecond) /  1000000
    time.sleep(timeToWait)

