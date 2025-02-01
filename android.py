#!/bin/python3
import time
import subprocess


from newProvider import sch, cycleDay, pl2 # Bad code, fix later
import datetime as dt

import setproctitle
setproctitle.setproctitle("dailyinfod")

# import config

cycleDayStr = str(cycleDay)

def upntf(title, contents):
    subprocess.run(["termux-notification", "-t", title, "-c", contents, "--icon", "filter_"+cycleDayStr, "--id", "8363", "--ongoing", "--button1", "dismiss", "--button1-action", "killall dailyinfod; sleep 0.1 && termux-notification-remove 8363"])

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
                upntf(summary, sch.getPeriodName() + " " + sch.getPeriodSymbol() + " " + str(timeLeft))
                time.sleep(20)
            else:
                upntf(summary, sch.getPeriodSymbol() + " → " + sch.getPeriodName(lookahead=1) + " " + sch.getPeriodSymbol(lookahead=1) + " " + str(sch.getPeriodTimeTil(lookahead=1)))
                time.sleep(1)
        except:
            upntf(summary, summary2)
            break
    else:
        upntf(summary, "Wait → " + sch.getPeriodName() + " " + sch.getPeriodSymbol() + " " + str(sch.getPeriodTimeTil()))
        time.sleep(1)

