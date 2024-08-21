# System
import datetime as dt
import time

# User
import calRead
import schedule
import newconfig as config

if config.cycle_day_override is not None:
    assert 1 <= config.cycle_day_override <= 8
    cycleDay = config.cycle_day_override
else:
    offset = config.date_offset
    if offset is None:
        offset = 0
    
    cycleDay = calRead.cycleDay(offset, verbose=True)


currentDatetime = dt.datetime.now() # do not change since otherwise it will not work

# Check day of week

if config.weekday_override is not None:
    weekday = config.weekday_override
else:
    weekday = currentDatetime.weekday()
'''
match weekday:
    case 2:
        isWednesday = True
    case 5:
        isWeekday = False
    case 6:
        isWeekday = False
'''




if config.period_list_override is not None:
    pl = config.period_list_override
else:
    pl: list = schedule.generatePeriodList(config.base_period_list, cycleDay, isWednesday = (weekday == 2), 
                                 datetimesOverrideFunction = config.datetimes_override_function,
                                 durationsOverrideFunction = config.durations_override_function,
                                 periodOrderOverride = config.period_order_override,
                                 periodIndexListOverride = config.period_index_list_override
                                 )

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
