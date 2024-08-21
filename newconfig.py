# Important: do not delete any of those variables or error may occur
# Todo: import defaultConfig.py

import datetime as dt

_ = dt

date_offset: int = 9
cycle_day_override: int | None = None
day_end_time: str = "not implemented yet- ignore"
weekday_override: int | None = 0 # 0 is monday, useful if a day follows non-wednesday schedule



base_period_list = [ # For day I schedule
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
