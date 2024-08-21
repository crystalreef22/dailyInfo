# System
import argparse
import datetime as dt
import time

# User
import calRead
import schedule
import newconfig as config

parser = argparse.ArgumentParser(
                    prog='dailyInfo provider',
                    description='Provides daily information for school schedule') #,epilog='txt at end of help')

parser.add_argument('--dateoffset', type=int)
parser.add_argument('--cycleday', type=int, help="override cycle day. Takes precedance over any prompt args")
parser.add_argument('--dayendtime', type=str, help="not implemented")
parser.add_argument('-p', '--prompt_offset', type=str, help="y,Y,yEs,trUe/n,N,nO,faLse")
parser.add_argument('--prompt_cycleday', type=str, help="y,Y,yEs,trUe/n,N,nO,faLse")

args = parser.parse_args()


if args.cycleday is not None:
    cycleDay = args.cycleday
else:
    offset = args.dateoffset
    if offset is None:
        offset = 0
    
    if args.prompt_offset is None:
        pb = config.prompt_offset
        assert type(pb) is bool
        print("args.prompt is default is", pb)
    elif args.prompt_offset.lower() in ['y','yes','true']:
        print("args.prompt is true")
        pb = True
    elif args.prompt_offset.lower() in ['n','no','false']:
        print("args.prompt is false")
        pb = False
    else:
        pb = config.prompt_offset
        assert type(pb) is bool
        print("args.prompt is default is", pb)

    if pb:
        try:
            offset = int(input("offset > "))
        except:
            print("-> 0")


    cycleDay = calRead.cycleDay(offset, verbose=True)

# Check day of week

weekday = dt.datetime.now().weekday()
'''
match weekday:
    case 2:
        isWednesday = True
    case 5:
        isWeekday = False
    case 6:
        isWeekday = False
'''


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


pl = schedule.generatePeriodList(dayISchedulePeriodList, cycleDay, isWednesday = (weekday == 2))
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
            print("fixme: error on newProvider.py line 115")
            break
    else:
        print("Wait →", sch.getPeriodName(), sch.getPeriodSymbol(), sch.getPeriodTimeTil(), "               ", end="\r")

    time.sleep(0.05)
