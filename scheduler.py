import numpy as np
import calendar as cal


class Cal7:
    week_am = np.zeros((7,), dtype=int)
    week_pm = np.zeros((7,), dtype=int)


class Provider:
    def __init__(self, provider_name, specialty, clinic_preference, am_day_preferences, pm_day_preferences, days_off,
                 total_available_hours):
        self.provider_name = provider_name
        self.specialty = specialty  # [Child,Adult,Family] Preferences will be indicated by 1
        self.clinic_preference = clinic_preference  # [Clinic1,Clinic2,Clinic3] Preference will be indicated by 1
        self.am_day_preferences = am_day_preferences  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.pm_day_preferences = pm_day_preferences  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.days_off = days_off  # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.total_available_hours = total_available_hours


class Clinic:
    def __init__(self, clinic_name, min_staff, optimal_staff, max_staff):
        self.clinic_name = clinic_name
        self.min_staff = min_staff
        self.optimal_staff = optimal_staff
        self.max_staff = max_staff


# caltest = cal7()

# caltest.week[0][0] = 'Ben'
# caltest.week[0][1] = 'Alex'
# print(caltest.week[0])


p1 = Provider("John", 1, 2, [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], 40)
p2 = Provider("Jane", 0, 1, [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0], 40)
c1 = Clinic("Clinic1", 1, 2, 3)
c2 = Clinic("Clinic2", 1, 2, 3)


