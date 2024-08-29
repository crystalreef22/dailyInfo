import requests
import icalendar
from datetime import datetime, timedelta
from newconfig import calRead_link, calRead_Lstrip

def printIf(condition, *args, end='\n', sep=' ', flush=False):
    if condition:
        print(*args, end=end, sep=sep, flush=flush)

def cycleDay(dDay=0, verbose=False):
    url = calRead_link

    # Fetch the iCal file
    response = requests.get(url, timeout=10)

    # Check if the request was successful
    if response.status_code == 200:
        calendar_data = response.text

        # Parse the iCal data
        calendar = icalendar.Calendar.from_ical(calendar_data)

        # Get today's date
        today = datetime.now().date()+timedelta(days=dDay)


        # Iterate over calendar events
        for component in calendar.walk():
            if component.name == 'VEVENT':
                summary = component.get('summary')
                start = component.get('dtstart')

                # Check if it occurs today
                if start.dt == today:
                    printIf(verbose,f"cal: Event: {summary}")
                    try:
                        cycle=int(summary.lstrip(calRead_Lstrip))
                        printIf(verbose, f"cal: extracted day: {cycle}")
                        if not (0 < cycle < 9):
                            printIf(verbose,"oh no. Cycle day outofRange")
                        return cycle
                    except:
                        printIf(verbose,"cal: could not extract: no school?")
        else:
            printIf(verbose,"no events")

    else:
        raise Exception(f"cal: Failed to fetch iCal file. Status code: {response.status_code}")
    
    raise Exception(f"cal: Nothing returned")


