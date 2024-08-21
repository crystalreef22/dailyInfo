# Important: do not delete any of those variables or error may occur
# Todo: import defaultConfig.py

date_offset: int = 0
cycle_day_override: int | None = None
day_end_time: str = "not implemented yet- ignore"
weekday_override: int | None = None # 0 is monday, useful if a day follows non-wednesday schedule



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

period_list_override = None # i forgot how to use this. Overrides ALL config vars for generating period list
