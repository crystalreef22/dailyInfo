from datetime import datetime
# strptime all of it

class period:
    def __init__(self, cDay, isWednesday, ealunch = False):
        self.ealunch = ealunch
        self.cDay = cDay
        self.isWednesday = isWednesday
        self.calculateTimes() # Sets self.times
            
    def calculateTimes(self):
        ties = ["8:15","9:10","10:05","10:35","11:50","12:25" if self.ealunch else "12:40", "13:20","14:15", "15:05", "15:35"]
        if self.isWednesday:
            ties = ["9:35", "10:30","11:25", "12:20", "12:45" if self.ealunch else "13:10", "13:40", "14:35", "15:30"]

        self.times =  [datetime.strptime(x,"%H:%M").time() for x in ties]
    

if __name__ == "__main__":
    perd = period(1j, False)
    print(perd.times)
