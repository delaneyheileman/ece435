import numpy as np
import pandas as pd
import holidays
import datetime
from calendar import monthrange


def find_next_monday():
    today = datetime.date.today()
    if (today.weekday() == 0):
        year = today.strftime("%Y")
        month = today.strftime("%m")
        today = today.strftime("%d")
        return today, month, year
    else:
        for d in range(7):
            day = today + datetime.timedelta(days=d)
            if (day.weekday() == 0):
                year = day.strftime("%Y")
                month = day.strftime("%m")
                day = day.strftime("%d")
                return day, month, year

Dstart, Mstart, Cyear = find_next_monday()
day_start, month_start, year = int(Dstart), int(Mstart), int(Cyear)
day_start = 28
day_end = day_start + 13
if (monthrange(year, month_start)[1] - day_start) > 14:
    month_end = month_start
else:
    month_end = month_start + 1
    if day_end > monthrange(year, month_start)[1]:
        day_end = day_end - monthrange(year, month_start)[1]
print("day_start = ", day_start)
print("month_start = ", month_start)
print("year = ", year)
print("day_end = ", day_end)
# print("day =",day)
# print("today =",today)

# generates a calender based on inputs above

def calendar_generator(Year, Start_Month, End_Month, Start_Day, End_Day):
    us_holidays = []  # array for holidays

    # finds federal holidays in specified year
    for date in holidays.UnitedStates(years=Year).items():
        us_holidays.append(str(date[0]))

    # creates a time frame based on inputs
    start_date = datetime.datetime(year=Year, month=Start_Month, day=Start_Day)
    end_date = datetime.datetime(year=Year, month=End_Month, day=End_Day)

    print("start_date = ",start_date)
    print("end_date = ",end_date)
    # creates data frame and adds holidays to time frame. Final result is a two week period with federal holidays
    date_frame = pd.DataFrame()
    date_frame["Dates"] = pd.date_range(start_date, end_date)
    date_frame.head()
    date_frame["Is_Holiday"] = [1 if str(val).split()[0] in us_holidays else 0 for val in date_frame["Dates"]]
    date_frame.head()
    print("date_frame =", date_frame)
    return date_frame



find_next_monday()
calendar_generator(year, month_start, month_end, day_start, day_end)

