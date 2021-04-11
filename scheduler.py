import numpy as np
import calendar as cal

class cal7:
    week = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

caltest = cal7()

caltest.week[0][0] = 'Ben'
caltest.week[0][1] = 'Alex'

print(caltest.week[0])


class provider:
    def __init__(self, provider_name, specialty, clinic_preference, am_day_preferences, pm_day_preferences, days_off,
                 total_available_hours):

        self.provider_name = provider_name
        self.specialty = specialty                        # [Child,Adult,Family] Preferences will be indicated by 1
        self.clinic_preference =  [0,0,0]                 # [Clinic1,Clinic2,Clinic3] Preference will be indicated by 1
        self.am_day_preferences = [0,0,0,0,0,0,0]                   # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.pm_day_preferences = [0,0,0,0,0,0,0]                   # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.days_off = [0,0,0,0,0,0,0]                             # [M,T,W,T,F,S,S] Preference will be indicated by 1
        self.total_available_hours = 40

class clinic:

    def __init__(self,clinic_name, min_staff, optimal_staff, max_staff):

        self.clinic_name = 'Name'
        self.min_staff = 0
        self.optimal_staff = 0
        self.max_staff = 0


p1 = provider('john',[0,1,0])







