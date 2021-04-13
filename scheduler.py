import string
import numpy as np
import calendar as cal


class Cal7:
    week = np.empty(shape=(7, 2, 3), dtype='object')


class Provider:
    def __init__(self, provider_name, specialty, clinic_day_preference, days_off,
                 total_available_hours):
        self.provider_name = provider_name
        self.specialty = specialty  # Child = 0, Adult = 1, Family = 2
        self.clinic_day_preference = clinic_day_preference  # Indicate clinic preference 1-3 on days 0-6; 0 for off day; 4 no preference
        self.days_off = days_off  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.total_available_hours = total_available_hours


class Clinic:
    def __init__(self, clinic_name, min_ped, min_aud, idl_ped, idl_aud, max_staff, calendar):
        self.clinic_name = clinic_name
        self.min_ped = min_ped
        self.min_aud = min_aud
        self.idl_ped = idl_ped
        self.idl_aud = idl_aud
        self.max_staff = max_staff
        self.calendar = calendar
        self.ped_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.aud_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.max_counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.specialty_list = [0, 0] * max_staff

    def specialty_incrementer(self, specialty, d, s):
        if specialty == 0:
            self.ped_counter[d][s] += 1
            self.max_counter[d][s] += 1
        elif specialty == 1:
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1
        else:
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1

    def staff_logic(self, specialty, d, s):

        if specialty == 0 and self.ped_counter[d][s] <= self.idl_ped and self.max_counter[d][s] <= self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == 1 and self.aud_counter[d][s] <= self.idl_aud and self.max_counter[d][s] <= self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == 2 and self.aud_counter[d][s] <= self.idl_aud and self.max_counter[d][s] <= self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        else:
            return False


class Satellite_clinic(Clinic):
    def specialty_incrementer(self, specialty, d, s):
        if specialty == 0:
            self.ped_counter[d][s] += 1
            self.max_counter[d][s] += 1
        elif specialty == 1:
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1
        else:
            self.ped_counter[d][s] += 1
            self.aud_counter[d][s] += 1
            self.max_counter[d][s] += 1

    def staff_logic(self, specialty, d, s):

        if specialty == 0 and self.max_counter[d][s] < self.max_staff and self.aud_counter[d][s] >= self.min_aud:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == 1 and self.max_counter[d][s] < self.max_staff and self.ped_counter[d][s] >= self.min_ped:
            self.specialty_incrementer(specialty, d, s)
            return True
        elif specialty == 2 and self.max_counter[d][s] < self.max_staff:
            self.specialty_incrementer(specialty, d, s)
            return True
        else:
            return False


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


# def __init__(self, provider_name, specialty, clinic_day_preference, days_off, total_available_hours):

p1 = Provider("Colgan", 0, [[0, 0], [1, 1], [1, 1], [0, 0], [0, 0], [1, 1], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p2 = Provider("Jones", 0, [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p3 = Provider("Zelleke", 0, [[0, 0], [0, 0], [0, 0], [0, 1], [1, 1], [2, 2], [0, 0]], [0, 1, 1, 0, 0, 0, 0], 40)
p4 = Provider("Fraser", 2, [[0, 0], [0, 0], [0, 1], [0, 0], [0, 1], [1, 1], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p5 = Provider("Garza", 2, [[0, 0], [1, 1], [1, 0], [0, 1], [1, 0], [0, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p6 = Provider("Haley", 2, [[0, 0], [2, 2], [2, 2], [0, 2], [0, 0], [0, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p7 = Provider("Veal", 2, [[0, 0], [3, 3], [3, 3], [0, 3], [3, 3], [0, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p8 = Provider("Wilkerson", 2, [[0, 0], [0, 0], [0, 1], [0, 0], [1, 0], [1, 1], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p9 = Provider("Littlejohn", 2, [[0, 0], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)
p10 = Provider("Willie", 1, [[0, 0], [0, 0], [2, 2], [0, 0], [0, 0], [0, 0], [0, 0]], [0, 0, 0, 0, 0, 0, 0], 40)

cc1 = np.empty(shape=(7, 2, 3), dtype='object')
cc2 = np.empty(shape=(7, 2, 3), dtype='object')
cc3 = np.empty(shape=(7, 2, 3), dtype='object')

# def __init__(self, clinic_name, min_ped, min_aud, idl_ped, idl_aud, max_staff, calendar):
c1 = Clinic(1, 1, 1, 2, 3, 5, cc1)
c2 = Satellite_clinic(2, 1, 1, 3, 3, 3, cc2)
c3 = Satellite_clinic(3, 1, 1, 3, 3, 3, cc3)


Provider_List = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
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
                    if provider.clinic_day_preference[day][shift] == clinic.clinic_name:
                        if provider.days_off[day] == 0:
                            if provider.total_available_hours >= 4:
                                if clinic.calendar[day][shift][slot] is None and provider.provider_name not in \
                                        clinic.calendar[day][shift]:
                                    if clinic.staff_logic(provider.specialty, day, shift):
                                        provider.total_available_hours = provider.total_available_hours - 4
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
