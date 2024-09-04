import datetime as dt
import time
import copy

class schedule:
    def __init__(self, periodList):
        self.periodList = periodList
        self.currentPeriodIndex = 0
        # self.currentDatetime
        self.updatePeriod()
    
    def getEaLunch(self):
        '''Returns optional bool (hopefully)'''
        try:
            assert self.periodList[-1]["type"] == "info"
            return self.periodList[-1]["eaLunch"]
        except KeyError:
            return None

    def updatePeriod(self) -> bool:
        '''return false if class has not started yet'''
        self.currentDatetime = dt.datetime.now()
        i = None
        for i, period in enumerate(self.periodList):
            # t = dt.datetime.combine(self.currentDatetime.date(), period["time"])
            if period["type"] == "info":
                i -= 1
                break
            
            t = period["datetime"]
            if t > self.currentDatetime:
                i -= 1;
                break

        if i is None:
            raise IndexError("PeriodList could not be iterated")

        # period = self.periodList[i]

        
        if i == -1:
            self.currentPeriodIndex = 0
            return False

        self.currentPeriodIndex = i
        return True

    def getPeriodTimeLeft(self, lookahead=0):
        period = self.periodList[self.currentPeriodIndex + lookahead]
        return period["datetime"] + period["duration"] - self.currentDatetime

    def getPeriodTimeTil(self, lookahead=0):
        period = self.periodList[self.currentPeriodIndex + lookahead]
        return period["datetime"] - self.currentDatetime

    def getCurrentPeriodIndex(self):
        return self.currentPeriodIndex
    
    def getPeriodName(self, lookahead = 0):
        return self.periodList[self.currentPeriodIndex + lookahead]["periodName"]
    
    def getPeriodSymbol(self, lookahead = 0):
        return self.periodList[self.currentPeriodIndex + lookahead]["periodSymbol"]
        














def generatePeriodList(dayISchedulePeriodList: list, cycleDay: int, isWednesday: bool = False, datetimesOverrideFunction = None, durationsOverrideFunction = None, periodOrderOverride = None, periodIndexListOverride = None, currentDate = None) -> list:
    '''
    periodOrderOverride: reorders the list as such: [1,2,3,4,5,6] or None is normal, [1,2,3,5,4,6] is period 5 and 4 switched, etc.
    periodIndexListOverride: controls how we take from the dayISchedulePeriodList: default is [0,3,6,4,7,10], corresponding to birdybirdybirdybird's method of +3, +3, -2, +3, +3
    timesOverrideFunction is a function with this form: someFunction(eaLunch), and it should return an array of datetime.time(), with the last time being the time class ends if durationsOverride is not active
    Durations will automatically be calculated unless durationsOverrideFunction exists, in which case it will act like timesOverrideFunction

    '''

    assert cycleDay >= 1 and cycleDay <= 8

    if currentDate is None:
        currentDate = dt.datetime.now().date()

    

    if periodIndexListOverride is None:
        periodOrder = [0,3,6,4,7,10]
        if periodOrderOverride is not None:
            tmp = [periodOrder[item-1] for item in periodOrderOverride]
            periodOrder = tmp
            del tmp

        periodIndexList = [(item + cycleDay - 1) % 8 for item in periodOrder]
    else:
        periodIndexList = periodIndexListOverride
    


    periodList = [copy.deepcopy(dayISchedulePeriodList[item]) for item in periodIndexList]

    
    try:
        eaLunch = periodList[3]["eaLunch"] # check period 4
        print("eal", periodList[3])
    except KeyError:
        eaLunch = None # Just a dummy value, does not matter anyway

    
    

    # Fixme: this part does not work
    if datetimesOverrideFunction is None:
        ties =     ["8:15", "9:10","10:05","10:35","11:50", "12:25" if eaLunch else "12:45", "13:20", "14:15", "15:05", "15:35"]
        if isWednesday:
            ties = ["9:35","10:30","11:25","11:25","12:20", "12:45" if eaLunch else "13:15", "13:40", "14:35", "15:30", "15:30"]

        times =  [dt.datetime.combine(currentDate, dt.datetime.strptime(x,"%H:%M").time()) for x in ties]

    else:
        times = datetimesOverrideFunction(eaLunch)

    if durationsOverrideFunction == None:
        durations = []
        # Now set up durations automatically
        for i in range(len(times) - 1):
            durations.append(times[i+1] - times[i] - dt.timedelta(minutes=5))
    else:
        durations = durationsOverrideFunction(eaLunch)

    
    # now loop through periodList and add times and touchups like removal of free periods and expansion of double sciences if applicable, and period number
    ip = 0
    for i in range(len(periodList)):
        if i in [2,3 if eaLunch else 4]:
            ip += 1
        periodList[i]["datetime"] = times[i + ip]
        periodList[i]["duration"] = durations[i + ip]
        periodList[i]["type"] = "standard"
        periodList[i].pop("eaLunch", None)

    
    finalPeriodList = []
    for i in range(len(periodList)):
        if i == 2:
            if durations[2] >= dt.timedelta(0):
                finalPeriodList.append(
                    {
                        "datetime": times[2],
                        "duration": durations[2],
                        "type": "clubOrAssembly",
                        "periodName" : "club or assembly",
                        "periodSymbol" : "🏛️",
                    })
            else:
                print("!!!!!!!!!!!!!!!!! Skipping club period")
        if i == (3 if eaLunch else 4):
            if durations[i+1] >= dt.timedelta(0):
                finalPeriodList.append(
                    {
                        "datetime": times[i + 1],
                        "duration": durations[i + 1],
                        "type": "lunch",
                        "periodName": "Lunch",
                        "periodSymbol": "🍽️",
                    }
                )
        finalPeriodList.append(periodList[i])
        

    finalPeriodList.append(
        {
            "type":"info",
            "eaLunch": eaLunch,
        }
    )

    return finalPeriodList


