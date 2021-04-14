import numpy as np
import pandas as pd
import holidays
import datetime

year = 2021
month_start = 1
month_end = 1
day_start = 17
day_end = 23


def calendar_generator(Year, Start_Month, End_Month, Start_Day, End_Day):
    us_holidays = []

    for date in holidays.UnitedStates(years=Year).items():
        us_holidays.append(str(date[0]))

    start_date = datetime.datetime(year=Year, month=Start_Month, day=Start_Day)
    end_date = datetime.datetime(year=Year, month=End_Month, day=End_Day)
    date_frame = pd.DataFrame()
    date_frame["Dates"] = pd.date_range(start_date, end_date)
    date_frame.head()
    date_frame["Is_Holiday"] = [1 if str(val).split()[0] in us_holidays else 0 for val in date_frame["Dates"]]
    date_frame.head()
    return date_frame


class Provider:
    def __init__(self, provider_name, specialty, day_preferences, total_available_hours):
        self.provider_name = provider_name
        self.specialty = specialty
        self.day_preferences = day_preferences
        self.total_available_hours = total_available_hours
        self.week = np.empty(shape=(7, 2), dtype="object")


class Clinic:
    def __init__(self, clinic_name, min_ped, min_aud, idl_ped, idl_aud, max_staff):
        self.clinic_name = clinic_name
        self.min_ped = min_ped
        self.min_aud = min_aud
        self.idl_ped = idl_ped
        self.idl_aud = idl_aud
        self.max_staff = max_staff
        self.ped_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.aud_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.max_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.week = np.empty(shape=(7, 2, 3), dtype="object")

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


class Satellite_clinic(Clinic):
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


def clinic_printer(clnc):
    out = np.transpose(clnc)
    out = np.array(out)

    print("AM")
    print(out[0][0])
    print(out[1][0])
    print(out[2][0])
    print("\nPM")
    print(out[0][1])
    print(out[1][1])
    print(out[2][1])


def provider_printer(clnc):
    out = np.transpose(clnc)
    out = np.array(out)
    print("AM")
    print(out[0][:])
    print("\nPM")
    print(out[1][:])


calendar = calendar_generator(year, month_start, month_end, day_start, day_end)


def scheduler(Provider_List, Clinic_List):

    weekdays = [0, 1, 2, 3, 4, 5, 6]
    shifts = [0, 1]
    slots = [0, 1, 2]

    for day in weekdays:
        for clinic in Clinic_List:
            for shift in shifts:
                for slot in slots:
                    for provider in Provider_List:
                        if calendar.index[calendar["Is_Holiday"] == 1].values[0] == day:
                            clinic.week[day][:][:] = "Holiday"
                        if provider.day_preferences[day][shift] != clinic.clinic_name:
                            provider.week[day][shift] = provider.day_preferences[day][shift]
                        else:
                            if provider.total_available_hours >= 4:
                                if clinic.week[day][shift][slot] is None and provider.provider_name not in \
                                        clinic.week[day][shift]:
                                    if clinic.staff_logic(provider.specialty, day, shift):
                                        provider.total_available_hours = provider.total_available_hours - 4
                                        clinic.week[day][shift][slot] = provider.provider_name
                                        provider.week[day][shift] = provider.day_preferences

    for clinic in Clinic_List:
        print("\n")
        print(clinic.clinic_name)
        clinic_printer(clinic.week)

    # for provider in Provider_List:
    #     print("\n")
    #     print(provider.provider_name)
    #     provider_printer(provider.week)