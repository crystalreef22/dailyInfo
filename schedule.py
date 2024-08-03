import datetime as dt

def timePlusDelta(time, timedelta):
    return (dt.datetime.combine(dt.date(1,1,1),time) + timedelta).time()

class schedule:
    def __init__(self, periodList):
        self.periodList = periodList
        self.currentPeriodIndex = 0
        self.periodTimeLeft
        self.currentTime
        self.updatePeriod()
    
    def updatePeriod(self, testDeltaTime = dt.timedelta(0)) -> None:
        self.currentTime = (dt.datetime.now() + testDeltaTime).time()
        for i, period in enumerate(self.periodList):
            t = period["time"]
            if t > self.currentTime:
                break
        else:
            raise IndexError("PeriodList could not be iterated")
        
        self.currentPeriodIndex = i
        self.periodTimeLeft = timePlusDelta(period["time"], period["duration"]) - self.currentTime

    def getPeriodTimeLeft(self):
        return self.periodTimeLeft

    def getCurrentPeriodIndex(self):
        return self.currentPeriodIndex
    
    def getPeriodName(self, lookahead = 0):
        return self.periodList[self.currentPeriodIndex + lookahead]["periodName"]
    
    def getPeriodSymbol(self, lookahead = 0):
        return self.periodList[self.currentPeriodIndex + lookahead]["periodSymbol"]

    def periodIsOver(self):
        return self.periodTimeLeft < dt.timedelta(0)
        


if __name__=="__main__":
    periodList = [
            {
                "time":dt.time(8,15), #8:05 AM
                "duration": dt.timedelta(minutes=50),
                "periodName":"Composing",
                "periodSymbol":"🎻",
            },
            {
                "time":dt.time(9,10),
                "duration": dt.timedelta(minutes=50),
                "periodName":"Computer Scinece",
                "periodSymbol":"💻",
            },
            {
                "time":dt.time(10,35),
                "duration": dt.timedelta(hours=1, minutes=10),
                "periodName":"Wayfinding",
                "periodSymbol":"🧭",
            },
            {
                "time":dt.time(12,25),
                "duration": dt.timedelta(minutes=50),
                "periodName":"Division 201",
                "periodSymbol":"🧭",
            },
            {
                "time":dt.time(13,20),
                "duration": dt.timedelta(minutes=50),
                "periodName":"Cryptography II",
                "periodSymbol":"📜",
            },
            {
                "time":dt.time(14,15),
                "duration": dt.timedelta(minutes=45),
                "periodName":"Potion-making",
                "periodSymbol":"🧪",
            },
    ]
    sch = schedule(periodList)
