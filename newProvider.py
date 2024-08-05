# System
import argparse
import datetime as dt
import time

# User
import calRead
import schedule

parser = argparse.ArgumentParser(
                    prog='dailyInfo provider',
                    description='Provides daily information for school schedule') #,epilog='txt at end of help')

parser.add_argument('--dateoffset', type=int)
parser.add_argument('--cycleday', type=int, help="override cycle day")
parser.add_argument('--nextdaytime', type=str, help="not implemented")
parser.add_argument('-p', '--prompt',
                    action='store_true')

args = parser.parse_args()


if args.cycleday is not None:
    cycleDay = args.cycleday
else:
    offset = args.dateoffset
    if offset is None:
        offset = 0

    if args.prompt:
        try:
            offset = int(input("offset > "))
        except:
            print("-> 0")
    cycleDay = calRead.cycleDay(offset, verbose=True)

# Check day of week
isWeekday = True
isWednesday = False    
match dt.datetime.now().weekday():
    case 2:
        isWednesday = True
    case 5:
        isWeekday = False    
    case 6:
        isWeekday = False



dayISchedulePeriodList = [
        {
            "eaLunch": True,
            "periodName":"Composing",
            "periodSymbol":"🎻",
        },
        {
            "eaLunch": True,
            "periodName":"Computer Scinece",
            "periodSymbol":"💻",
        },
        {
            "eaLunch": True,
            "periodName":"Wayfinding",
            "periodSymbol":"🧭",
        },
        {
            "eaLunch": False,
            "periodName":"Division 201",
            "periodSymbol":"➗",
        },
        {
            "eaLunch": False,
            "periodName":"Cryptography II",
            "periodSymbol":"📜",
        },
        {
            "eaLunch": True,
            "periodName":"Potion-making",
            "periodSymbol":"🧪",
        },
        {
            "eaLunch": False,
            "periodName":"Magic Charms 101",
            "periodSymbol":"🪄",
        },
        {
            "periodName":"Free",
            "periodSymbol":"🆓",
        },
]


pl = schedule.generatePeriodList(dayISchedulePeriodList, cycleDay, isWednesday)
for i in pl:
    print(i)
for i in pl:
    if i["type"] != "info":
        print(i["datetime"], i["duration"])

sch = schedule.schedule(pl)

print("eaLunch:",sch.getEaLunch())

for i in range(-700,120):
    classHasStarted = sch.updatePeriod(testDeltaTime=dt.timedelta(minutes = i))
    if classHasStarted:
        timeLeft = sch.getPeriodTimeLeft()
        try:
            if timeLeft >= dt.timedelta(0):
                print(sch.getPeriodName(), sch.getPeriodSymbol(), timeLeft, "               ", end="\r")
            else:
                print(sch.getPeriodSymbol(), "→", sch.getPeriodName(lookahead=1), sch.getPeriodSymbol(lookahead=1), sch.getPeriodTimeTil(lookahead=1), "               ", end="\r")
        except:
            print("fixme: error on newProvider.py line 116")
            break
    else:
        print("Wait →", sch.getPeriodName(), sch.getPeriodSymbol(), sch.getPeriodTimeTil(), "               ", end="\r")

    time.sleep(0.05)
