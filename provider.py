#!/bin/python
from calRead import cycleDay
from config import PERIODS, SCHEDULE, cdDay, TODAYSCHEDOVERRIDE, LATELUNCH
# calender studf
cDay=cycleDay(cdDay)
#DONT FORGET TO SUBTRACT ONE!
infotext = ""

#idk later
# https://forecast.weather.gov/meteograms/Plotter.php?lat=40.543&lon=-79.8026&wfo=PBZ&zcode=PAZ021&gset=20&gdiff=10&unit=0&tinfo=EY5&ahour=0&pcmd=11101111110000000000000000000000000000000000000000000000000&lg=en&indu=1!1!1!&dd=&bw=&hrspan=36&pqpfhr=6&psnwhr=6

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


