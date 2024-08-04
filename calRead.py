import requests
import icalendar
from datetime import datetime, timedelta

def cycleDay(dDay=0):
    url = "https://site redacted/calendar/calendar_7187.ics"

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
                    print(f"cal: Event: {summary}")
                    try:
                        cycle=int(summary.lstrip("SS Cycle Day "))
                        print(f"cal: extracted day: {cycle}")
                        if not (0 < cycle < 9):
                            print("oh no. Cycle day outofRange")
                        return cycle
                    except:
                        print("cal: could not extract: no school?")
        else:
            print("no events")

    else:
        raise Exception(f"cal: Failed to fetch iCal file. Status code: {response.status_code}")
    
    raise Exception(f"cal: Nothing returned")


