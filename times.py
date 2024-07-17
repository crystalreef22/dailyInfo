from datetime import datetime
# strptime all of it

class period:
    def __init__(cDay, isWednesday, ealunch = false):
        calculateTimes()
            
    def calculateTimes(self):
        ties = ["8:15","9:10","10:05","10:35","11:50","12:25" if self.ealunch else "12:40", "13:20","14:15", "15:05", "15:35"]
        if self.isWednesday:
            ties = ["9:35", "10:30","11:25", "12:20", "12:45" if self.ealunch else "13:10", "13:40", "14:35", "15:30"]

        return [datetime.strptime(x,"%H:%M").time() for x in ties]

