from datetime import datetime
from config import TIMES
from config import WENDTIMES
# strptime all of it

def calculateTimes(cDay, isWednesday, hasEarlyLunch = False):
    times = ["8:15","9:10","10:05","10:35","11:50","12:25" if ealunch else "12:40", "1:20","2:15", "3:05", "3:35"]
    if isWednesday:
        times = ["9:35", "10:30","11:25", "12:20", "12:45" if ealunch else "1:10", "1:40", "2:35", "3:30"]
