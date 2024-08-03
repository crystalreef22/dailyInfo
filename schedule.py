import datetime as dt
import time

class schedule:
    def __init__(self, periodList):
        self.periodList = periodList
        self.currentPeriodIndex = 0
        # self.periodTimeLeft
        # self.currentDatetime
        self.updatePeriod()
    
    def updatePeriod(self, testDeltaTime = dt.timedelta(0)) -> None:
        self.currentDatetime = dt.datetime.now() + testDeltaTime
        i = None
        for i, period in enumerate(self.periodList):
            t = dt.datetime.combine(self.currentDatetime.date(), period["time"])
            if t > self.currentDatetime:
                i -= 1;
                break

        if i is None:
            raise IndexError("PeriodList could not be iterated")

        period = self.periodList[i]
        
        self.currentPeriodIndex = i
        self.periodTimeLeft = dt.datetime.combine(self.currentDatetime.date(), period["time"]) + period["duration"] - self.currentDatetime

    def getPeriodTimeLeft(self):
        return self.periodTimeLeft

    def getCurrentPeriodIndex(self):
        return self.currentPeriodIndex
    
    def getPeriodName(self, lookahead = 0):
        return self.periodList[self.currentPeriodIndex + lookahead]["periodName"]
    
    def getPeriodSymbol(self, lookahead = 0):
        return self.periodList[self.currentPeriodIndex + lookahead]["periodSymbol"]

    def getPeriodIsStillGoing(self):
        return self.periodTimeLeft >= dt.timedelta(0)
        


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
    for i in range(0,120):
        sch.updatePeriod(testDeltaTime=dt.timedelta(minutes = i))
        print(sch.getPeriodName(), sch.getPeriodSymbol(), sch.getPeriodTimeLeft(), sch.getPeriodIsStillGoing(), "          ", end="\r")
        time.sleep(0.2)
