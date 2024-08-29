# Important: do not delete any of those variables or error may occur
# Todo: import defaultConfig.py

import datetime as dt

_ = dt

date_offset: int = 0
cycle_day_override: int | None = None
weekday_override: int | None = None # 0 is monday, useful if a day follows non-wednesday schedule



base_period_list = [ # For day I schedule
        {
            "eaLunch": False,
            "periodName":"Orchestra",
            "periodSymbol":"🎻",
        },
        {
            "eaLunch": False,
            "periodName":"Computer Scinece",
            "periodSymbol":"💻",
        },
        {
            "eaLunch": None,
            "periodName":"Free",
            "periodSymbol":"🆓",
        },
        {
            "eaLunch": False,
            "periodName":"History",
            "periodSymbol":"🧭",
        },
        {
            "eaLunch": True,
            "periodName":"Calculus",
            "periodSymbol":"➗",
        },
        {
            "eaLunch": True,
            "periodName":"English",
            "periodSymbol":"📝",
        },
        {
            "eaLunch": False,
            "periodName":"Latin",
            "periodSymbol":"📜",
        },
        {
            "eaLunch": True,
            "periodName":"Biology",
            "periodSymbol":"🧬",
        },
]

calRead_Lstrip = "SS Cycle Day "
calRead_link = "https://site redacted/data/calendar/calendar_16475.ics"

datetimes_override_function = None # None or function(bool: eaLunch) -> list[dt.datetime]
durations_override_function = None # None for calculate from datetimes (with 5 minute passing) or
                                   # function(bool: eaLunch) -> list[timedelta]

period_order_override: list[int] | None = [1,2,3,4,5,6] # [1,2,3,4,5,6] means do nothing, [1,2,3,5,4,6]
                                                        # reverses period 5 and 4. Ignored if
                                                        # period_index_list_override is set.
period_index_list_override: list[int] | None = None # Order to pull periods from the day I schedule. Wraps.
                                                    # e.g. Day 1 schedule is [0,3,6,4,7,10], Day 2 is [1,4,7,...].

period_list_override = None # an example is provided below.

'''
period_list_override = [
     {
      'datetime': dt.datetime(2024, 8, 21, 8, 15),
      'duration': dt.timedelta(seconds=3000),
      'periodName': 'Wayfinding',
      'periodSymbol': '🧭',
      'type': 'standard'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 9, 10),
      'duration': dt.timedelta(seconds=3000),
      'periodName': 'Potion-making',
      'periodSymbol': '🧪',
      'type': 'standard'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 10, 5),
      'duration': dt.timedelta(seconds=1500),
      'periodName': 'club or assembly',
      'periodSymbol': '🏛️',
      'type': 'clubOrAssembly'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 10, 35),
      'duration': dt.timedelta(seconds=4200),
      'periodName': 'Composing',
      'periodSymbol': '🎻',
      'type': 'standard'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 11, 50),
      'duration': dt.timedelta(seconds=3000),
      'periodName': 'Magic Charms 101',
      'periodSymbol': '🪄',
      'type': 'standard'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 12, 45),
      'duration': dt.timedelta(seconds=1800),
      'periodName': 'Lunch',
      'periodSymbol': '🍽️',
      'type': 'lunch'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 13, 20),
      'duration': dt.timedelta(seconds=3000),
      'periodName': 'Computer Scinece',
      'periodSymbol': '💻',
      'type': 'standard'
     },
     {
      'datetime': dt.datetime(2024, 8, 21, 14, 15),
      'duration': dt.timedelta(seconds=2700),
      'periodName': 'Cryptography II',
      'periodSymbol': '📜',
      'type': 'standard'
     },
     {
      'eaLunch': False, 'type': 'info'
     }
]
'''


def d(h,m):
    return dt.datetime.combine(dt.date.today(), dt.time(h,m))

def t(m):
    return dt.timedelta(minutes=m)

