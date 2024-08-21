from newProvider import sch # Bad code, fix later
import datetime as dt
import time

# import newconfig as config

summary = "["

for i in sch.periodList:
    try:
        summary += i["periodSymbol"];
    except KeyError:
        pass

summary += "]"

while True:


    classHasStarted = sch.updatePeriod()
    if classHasStarted:
        timeLeft = sch.getPeriodTimeLeft()
        try:
            if timeLeft >= dt.timedelta(0):
                print(summary, sch.getPeriodName(), sch.getPeriodSymbol(), timeLeft, "               ", end="\r")
            else:
                print(summary, sch.getPeriodSymbol(), "→", sch.getPeriodName(lookahead=1), sch.getPeriodSymbol(lookahead=1), sch.getPeriodTimeTil(lookahead=1), "               ", end="\r")
        except:
            print("fixme: error on linux.py line 29")
            break
    else:
        print(summary, "Wait →", sch.getPeriodName(), sch.getPeriodSymbol(), sch.getPeriodTimeTil(), "               ", end="\r")

    timeToWait = (1000000 - sch.currentDatetime.microsecond) /  1000000
    time.sleep(timeToWait)

