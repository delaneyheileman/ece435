import string
import numpy as np
import calendar as cal


class Cal7:
    week = np.empty(shape=(7, 2, 3), dtype='object')


class Provider:
    def __init__(self, provider_name, specialty, clinic_preference, day_preferences, days_off,
                 total_available_hours):
        self.provider_name = provider_name
        self.specialty = specialty  # [Child,Adult,Family] Preferences will be indicated by 1
        self.clinic_preference = clinic_preference  # [Clinic1,Clinic2,Clinic3] Preference will be indicated by 1
        self.day_preferences = day_preferences  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.days_off = days_off  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.total_available_hours = total_available_hours


class Clinic:
    def __init__(self, clinic_name, min_staff, optimal_staff, max_staff, calendar):
        self.clinic_name = clinic_name
        self.min_staff = min_staff
        self.optimal_staff = optimal_staff
        self.max_staff = max_staff
        self.calendar = calendar


def printer(clnc):
    out = np.transpose(clnc)

    print("AM")
    print(out[0][0])
    print(out[1][0])
    print(out[2][0])
    print("\nPM")
    print(out[0][1])
    print(out[1][1])
    print(out[2][1])


p1 = Provider("John", 0, 0, [[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p2 = Provider("Jane", 0, 0, [[0, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p3 = Provider("Jill", 0, 0, [[1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p4 = Provider("Jake", 0, 0, [[1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p5 = Provider("Ben", 0, 0, [[1, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 1]], [0, 0, 0, 0, 0, 0, 0], 40)
p6 = Provider("Alex", 0, 0, [[0, 1], [0, 1], [0, 1], [0, 1], [0, 0], [0, 0], [0, 1]], [0, 0, 0, 0, 0, 0, 0], 40)
p7 = Provider("Derek", 0, 0, [[0, 1], [0, 1], [0, 0], [0, 0], [0, 1], [0, 1], [0, 1]], [0, 0, 0, 0, 0, 0, 0], 40)

p8 = Provider("Delaney", 0, 1, [[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p9 = Provider("Janner", 0, 1, [[0, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p10 = Provider("Alejandro", 0, 1, [[1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p11 = Provider("Billy", 0, 1, [[1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p12 = Provider("Bob", 0, 1, [[1, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 1]], [0, 0, 0, 0, 0, 0, 0], 40)
p13 = Provider("Margaret", 0, 1, [[0, 1], [0, 1], [0, 1], [0, 1], [0, 0], [0, 0], [0, 1]], [0, 0, 0, 0, 0, 0, 0], 40)
p14 = Provider("Adam", 0, 1, [[0, 1], [0, 1], [0, 0], [0, 0], [0, 1], [0, 1], [0, 1]], [0, 0, 0, 0, 0, 0, 0], 40)

p15 = Provider("Dennis", 0, 2, [[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p16 = Provider("Anne", 0, 2, [[0, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p17 = Provider("Ryan", 0, 2, [[1, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [1, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p18 = Provider("Charleston", 0, 2, [[1, 0], [1, 0], [0, 0], [0, 0], [1, 0], [1, 0], [1, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p19 = Provider("Nathan", 0, 2, [[1, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 1]], [0, 0, 0, 0, 0, 0, 0], 40)
p20 = Provider("Connor", 0, 2, [[0, 1], [0, 1], [0, 1], [0, 1], [0, 0], [0, 0], [0, 1]], [0, 0, 0, 0, 0, 0, 0], 40)
p21 = Provider("Anita", 0, 2, [[0, 1], [0, 1], [0, 0], [0, 0], [0, 1], [0, 1], [0, 1]], [0, 0, 0, 0, 0, 0, 0], 40)

cc1 = np.empty(shape=(7, 2, 3), dtype='object')
cc2 = np.empty(shape=(7, 2, 3), dtype='object')
cc3 = np.empty(shape=(7, 2, 3), dtype='object')
c1 = Clinic(0, 2, 5, 5, cc1)
c2 = Clinic(1, 1, 2, 3, cc2)
c3 = Clinic(2, 1, 2, 3, cc3)
# print(p1.provider_name,p1.specialty,p1.clinic_preference,p1.am_day_preferences[0], p1.calendar_am)

Provider_List = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21]
Clinic_List = [c1, c2, c3]

# provider location preference
# is provider available for shift
# does provider have available hour
# Shifts decrement total hour by 8


# loop from monday to sunday
#
# loop from clinic 1 to clinic 3
#
# loop from am to pm
#
# loop through staff list
# set specialty flag
# reduces totals hours for staff member by 8
# add assignment to staff and clinic  calendars  (staff assignment added to clinic day.shift.calendar array)
# stop at optimal staff

weekdays = [0, 1, 2, 3, 4, 5, 6]
shifts = [0, 1]
slots = [0, 1, 2]

for day in weekdays:
    for clinic in Clinic_List:
        for shift in shifts:
            for slot in slots:
                for provider in Provider_List:
                    if provider.clinic_preference == clinic.clinic_name:
                        if provider.day_preferences[day][shift] == 1:
                            if provider.days_off[day] == 0:
                                if provider.total_available_hours >= 8:
                                    if clinic.calendar[day][shift][slot] is None and provider.provider_name not in\
                                            clinic.calendar[day][shift]:
                                        provider.total_available_hours = provider.total_available_hours - 8
                                        clinic.calendar[day][shift][slot] = provider.provider_name

print("\n")
print("Clinic 1:")
printer(c1.calendar)

print("\n")
print("Clinic 2:")
printer(c2.calendar)

print("\n")
print("Clinic 3:")
printer(c3.calendar)


# print("Clinic 2: \n", printer(c2.calendar))
# printer(c2.calendar)


# print("clinic1\n" + str(np.transpose(c1.calendar)))
# out = np.transpose(c1.calendar)


# print("clinic1\n" + str(c1.calendar))
# print("\n")
# print("clinic2\n" + str(c2.calendar))
# print("\n")
# print("provider1\n" + str(p1.calendar))
# print("\n")
# print("provider2\n" + str(p2.calendar))
# print("\n")


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
