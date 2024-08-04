import datetime as dt
import time

class schedule:
    def __init__(self, periodList):
        self.periodList = periodList
        self.currentPeriodIndex = 0
        # self.currentDatetime
        self.updatePeriod()
    
    def getEaLunch(self):
        '''Returns optional bool (hopefully)'''
        try:
            return self.periodList[3]["eaLunch"] # check period 4
        except KeyError:
            return None

    def updatePeriod(self, testDeltaTime = dt.timedelta(0)) -> None:
        self.currentDatetime = dt.datetime.now() + testDeltaTime
        i = None
        for i, period in enumerate(self.periodList):
            # t = dt.datetime.combine(self.currentDatetime.date(), period["time"])
            t = period["datetime"]
            if t > self.currentDatetime:
                i -= 1;
                break

        if i is None:
            raise IndexError("PeriodList could not be iterated")

        period = self.periodList[i]
        
        self.currentPeriodIndex = i
    def getPeriodTimeLeft(self, lookahead=0):
        period = self.periodList[self.currentPeriodIndex + lookahead]
        return period["datetime"] + period["duration"] - self.currentDatetime

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


    periodList = [dayISchedulePeriodList[item] for item in periodIndexList]

    try:
        eaLunch = periodList[3]["eaLunch"] # check period 4
    except KeyError:
        eaLunch = False # Just a dummy value, does not matter anyway

    

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

    return periodList





if __name__=="__main__":
    if False:
        periodList = [
                {
                    "time":dt.time(8,15), #8:05 AM
                    "duration": dt.timedelta(minutes=50),
                    "periodName":"Composing",
                    "periodSymbol":"🎻",
                    "periodNumber": 1,
                },
                {
                    "time":dt.time(9,10),
                    "duration": dt.timedelta(minutes=50),
                    "periodName":"Computer Scinece",
                    "periodSymbol":"💻",
                    "periodNumber": 2,
                },
                {
                    "time":dt.time(10,35),
                    "duration": dt.timedelta(hours=1, minutes=10),
                    "periodName":"Wayfinding",
                    "periodSymbol":"🧭",
                    "periodNumber": 3,
                },
                {
                    "time":dt.time(12,25),
                    "duration": dt.timedelta(minutes=50),
                    "periodName":"Division 201",
                    "periodSymbol":"🧭",
                    "periodNumber": 4,
                },
                {
                    "time":dt.time(13,20),
                    "duration": dt.timedelta(minutes=50),
                    "periodName":"Cryptography II",
                    "periodSymbol":"📜",
                    "periodNumber": 5,
                },
                {
                    "time":dt.time(14,15),
                    "duration": dt.timedelta(minutes=45),
                    "periodName":"Potion-making",
                    "periodSymbol":"🧪",
                    "periodNumber": 6,
                },
        ]
        sch = schedule(periodList)
        for i in range(0,120):
            sch.updatePeriod(testDeltaTime=dt.timedelta(minutes = i))
            print(sch.getPeriodName(), sch.getPeriodSymbol(), sch.getPeriodTimeLeft(), sch.getPeriodIsStillGoing(), "          ", end="\r")
            time.sleep(0.2)
    
    if True:
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
        pl = generatePeriodList(dayISchedulePeriodList, 1)
        for i in pl:
            print(i)
        for i in pl:
            print(i["datetime"], i["duration"])

        sch = schedule(pl)

        print("eaLunch:",sch.getEaLunch())

        for i in range(-100,120):
            sch.updatePeriod(testDeltaTime=dt.timedelta(minutes = i))
            timeLeft = sch.getPeriodTimeLeft()
            print(sch.getPeriodName(), sch.getPeriodSymbol(), timeLeft, timeLeft >= dt.timedelta(0), "          ", end="\r")
            time.sleep(0.2)
