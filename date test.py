import numpy as np
import pandas as pd
import holidays
import datetime
from calendar import monthrange


def find_next_monday():
    today = datetime.date.today()
    if today.weekday() == 0:
        year = today.strftime("%Y")
        month = today.strftime("%m")
        today = today.strftime("%d")
        return today, month, year
    else:
        for d in range(7):
            day = today + datetime.timedelta(days=d)
            if day.weekday() == 0:
                year = day.strftime("%Y")
                month = day.strftime("%m")
                day = day.strftime("%d")
                return day, month, year


# generates a calender based on inputs above

def calendar_generator():
    dstart, mstart, cyear = find_next_monday()
    day_start, month_start, year = int(dstart), int(mstart), int(cyear)
    day_end = day_start + 13

    if (monthrange(year, month_start)[1] - day_start) > 14:
        month_end = month_start
    else:
        month_end = month_start + 1
        if day_end > monthrange(year, month_start)[1]:
            day_end = day_end - monthrange(year, month_start)[1]

    us_holidays = []  # array for holidays

    # finds federal holidays in specified year
    for date in holidays.UnitedStates(years=year).items():
        us_holidays.append(str(date[0]))

    # creates a time frame based on inputs
    start_date = datetime.datetime(year=year, month=month_start, day=day_start)
    end_date = datetime.datetime(year=year, month=month_end, day=day_end)

    # creates data frame and adds holidays to time frame. Final result is a two week period with federal holidays
    date_frame = pd.DataFrame()
    date_frame["Dates"] = pd.date_range(start_date, end_date)
    date_frame.head()
    date_frame["Is_Holiday"] = [1 if str(val).split()[0] in us_holidays else 0 for val in date_frame["Dates"]]
    date_frame.head()
    return date_frame

calendar = calendar_generator()

print(calendar)


