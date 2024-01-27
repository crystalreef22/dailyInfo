#!/bin/python
from calRead import cycleDay
from config import PERIODS, SCHEDULE, cdDay, TODAYSCHEDOVERRIDE, LATELUNCH
# calender studf
cDay=cycleDay(cdDay)
#DONT FORGET TO SUBTRACT ONE!
infotext = ""

#idk later
# weather info

print("p:day ", cDay)
print(PERIODS[cDay-1])

if TODAYSCHEDOVERRIDE == None:
    todaySched = []
    todaySchedAAAA =[]
    for i in PERIODS[cDay-1]:
        todaySched.append(SCHEDULE[i])
        todaySchedAAAA.append(i)
else:
    todaySched = TODAYSCHEDULEOVERRIDE


print(todaySched)
infotext += "Day "+str(cDay)+" | " + str(todaySched)

lalu = LATELUNCH[todaySchedAAAA[3]]

if lalu == 0:
    infotext += " | EaL"
elif lalu == 1:
    infotext += " | LaL"
elif lalu == 2:
    infotext += " | UnL"


