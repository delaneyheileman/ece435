import string
import numpy as np
import calendar as cal

class Output:

    output_provider_AM = np.zeros((7,), dtype=int)
    output_provider_PM = np.zeros((7,), dtype=int)


class Cal7:
    week_am = np.zeros((7,), dtype=int)
    week_pm = np.zeros((7,), dtype=int)



class Provider:
    def __init__(self, provider_name, specialty, clinic_preference, day_preferences, pm_day_preferences, days_off,
                 total_available_hours, calendar_am, calendar_pm):
        self.provider_name = provider_name
        self.specialty = specialty  # [Child,Adult,Family] Preferences will be indicated by 1
        self.clinic_preference = clinic_preference  # [Clinic1,Clinic2,Clinic3] Preference will be indicated by 1
        self.day_preferences = day_preferences  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.days_off = days_off  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.total_available_hours = total_available_hours
        self.calendar_am = calendar_am
        self.calendar_pm = calendar_pm

class Clinic:
    def __init__(self, clinic_name, min_staff, optimal_staff, max_staff, calendar_am, calendar_pm):
        self.clinic_name = clinic_name
        self.min_staff = min_staff
        self.optimal_staff = optimal_staff
        self.max_staff = max_staff
        self.calendar_am = calendar_am
        self.calendar_pm = calendar_pm


# caltest = cal7()

# caltest.week[0][0] = 'Ben'
# caltest.week[0][1] = 'Alex'
# print(caltest.week[0])


p1 = Provider("John", 1, 2, [[1,1], [0,1], [1,1], [0,0], [1,1], [0,0], [0,0]], [0, 0, 0, 0, 0, 0, 0], 40, Cal7.week_am, Cal7.week_pm)
p2 = Provider("Jane", 0, 1, [1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], 40,Cal7.week_am, Cal7.week_pm)
c1 = Clinic("Clinic1", 1, 2, 3, Cal7.week_am, Cal7.week_pm)
c2 = Clinic("Clinic2", 1, 2, 3, Cal7.week_am, Cal7.week_pm)

# print(p1.provider_name,p1.specialty,p1.clinic_preference,p1.am_day_preferences[0], p1.calendar_am)

Provider_List = [p1,p2]
Clinic_List = [c1,c2]


# provider location preferecene
# is provier available for shift
# does proiver have available hour
# Shifts decrement total hour by 8


#     loop from monday to sunday
#
#         loop from clinic 1 to clinic 3
#
#             loop from am to pm
#
#                 loop through staff list
#                     set specialty flag
#                     decriment totals hours for staff member
#                     add assignment to staff and clinic  calendars  (staff assingment appened to clinic day.shift.calendar array)
#                     stop at optimal staff

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
shifts = ['AM', 'PM']

for day in weekdays:

    for clinic in Clinic_List:

        for shift in shifts:

            for provider in Provider_List:
                if provider.clinic_preference == clinic:
                    if provider.day_preferences[day][shift] == [day,shift]:
                        if provider.am_day_preferences[][shift] == shift:




                # Specialty_Flag()
                # --l.total_available_hours



# def schedule_output(x):
# test = []
# for i in range(0, 6):
#     test.append([])
#
# test[0].append(p1.provider_name)
# if len(test[0]) == 3:
#     print('Optimal')
# print(test)




# if p1.day_preferences[1][1] == 1:
#     print(True)























