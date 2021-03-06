# ************************************************************************
# * This module produces the scheduler logic from input from inout
# *
# * COMPONENT NAME: scheduler.py
# *
# * VERSION: 3.0 (April 2021)
# *
# * Module Description
# * This module takes two arrays as inputs from inout and returns an array
# * to inout.
# * **********************************************************************/


import numpy as np
import pandas as pd
import holidays
import datetime
from calendar import monthrange
import inout


# This function finds the next monday from the day of program execution. This is done to sync with excel input
def find_next_monday():
    today = datetime.date.today()
    if today.weekday() == 0:
        return today
    else:
        for d in range(7):
            day = today + datetime.timedelta(days=d)
            if day.weekday() == 0:
                return day


# This function generates a 14 day calender based on object created by find_next_monday. This calendar includes holidays

def calendar_generator(startDate):
    day_start, month_start, year = int(startDate.day), int(startDate.month), int(startDate.year)
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


# class object of providers.
class Provider:
    def __init__(self, provider_name, specialty, day_preferences, shifts, priority):
        self.provider_name = provider_name
        self.specialty = specialty
        self.day_preferences = day_preferences
        self.shifts = shifts
        self.week = np.empty(shape=(14, 2), dtype="object")
        self.priority = priority


class Clinic:
    def __init__(self, clinic_name, min_ped, min_aud, idl_ped, idl_aud, max_staff):
        self.clinic_name = clinic_name
        # minimum requirements
        self.min_ped = min_ped
        self.min_aud = min_aud
        # ideal staff amounts
        self.idl_ped = idl_ped
        self.idl_aud = idl_aud
        self.max_staff = max_staff
        # counters for each specialty on each shift and day
        self.ped_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.aud_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.max_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        # clinic centric calendar days,shifts,amount of slots
        self.week = np.empty(shape=(14, 2, max_staff), dtype="object")

    # this class function increments clinic counters based on specialties
    def specialty_incrementer(self, specialty, d, s):
        if specialty == "PED":
            self.ped_counter[d][s] += 1
            self.max_counter[d][s] += 1
        elif specialty == "IM":
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1
        elif specialty == "FP":
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1

    # this class functions checks the clinic counter and the specialty of a provider to see if assignment is possible
    def staff_logic(self, specialty, d, s):

        if specialty == "PED" and self.ped_counter[d][s] <= self.idl_ped and self.max_counter[d][s] <= self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == "IM" and self.aud_counter[d][s] <= self.idl_aud and self.max_counter[d][s] <= self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == "FP" and self.aud_counter[d][s] <= self.idl_aud and self.max_counter[d][s] <= self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        else:
            return False


# clinic subclass for sub clinics (THS PPHC)
class Satellite_clinic(Clinic):

    # increments PED and AUD for family practice instead of just AUD
    def specialty_incrementer(self, specialty, d, s):
        if specialty == "PED":
            self.ped_counter[d][s] += 1
            self.max_counter[d][s] += 1
        elif specialty == "IM":
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1
        elif specialty == "FP":
            self.ped_counter[d][s] += 1
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1

    # staff logic for sub clinics
    def staff_logic(self, specialty, d, s):

        if specialty == "PED" and self.max_counter[d][s] < self.max_staff and self.aud_counter[d][s] >= self.min_aud:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == "IM" and self.max_counter[d][s] < self.max_staff and self.ped_counter[d][s] >= self.min_ped:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == "FP" and self.max_counter[d][s] < self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        else:
            return False


#  main function. This function calls all above functions to create a calendar based on inputs and logic defined in
#  clinic classes.
def scheduler(Provider_List, Clinic_List):
    nextMonday = find_next_monday()
    calendar = calendar_generator(nextMonday)
    weekdays = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    shifts = [0, 1]
    slots = [0, 1, 2]

    # First loops through all days within specified date range
    for day in weekdays:

        # Second, loops through all clinics in clinic list
        for clinic in Clinic_List:

            # Third, loops through AM, PM shifts
            for shift in shifts:

                # Forth, loops through all slots
                for slot in slots:

                    # Fifth, loops through all providers in provider list (list is randomized with priority 0 first
                    for provider in Provider_List:
                        # Checks if current day is a holiday, if it is assign holiday to all shifts and slots
                        if calendar.index[calendar["Is_Holiday"] == 1] == day:
                            clinic.week[day][:][:] = "Holiday"
                        # else if the current provider is not scheduled for current clinic put what they are scheduled
                        # for in their personal calendar
                        elif provider.day_preferences[day][shift] != clinic.clinic_name:
                            provider.week[day][shift] = provider.day_preferences[day][shift]
                        # else continue
                        else:
                            # checks if current provider has shifts left to work
                            if provider.shifts >= 1:
                                # checks if there is a slot available for the provider at the current clinic
                                if clinic.week[day][shift][slot] is None and provider.provider_name not in \
                                        clinic.week[day][shift]:
                                    # checks if the current clinic as room for current provider's specialty. If it
                                    # does decrement provider's available shifts and add them to the clinics calendar
                                    # and the provider's own calendar.
                                    if clinic.staff_logic(provider.specialty, day, shift):
                                        provider.shifts = provider.shifts - 1
                                        clinic.week[day][shift][slot] = provider.provider_name
                                        provider.week[day][shift] = provider.day_preferences
    # calls inout output to create output excel file.
    inout.outputClinicSchedule(Clinic_List, nextMonday)
