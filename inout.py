#last UD 5/4/2021 1:23 PM
import pandas as pd
import scheduler as sch
import datetime
import random

# randomizeProviders()
# Inputs:
#     inputList : a list of scheduler.Provider objects
# Outputs:
#     randomList : a list containing the elements of the input list in
#       psuedo-randomized order with priority 0 objects first

def randomizeProviders(inputList):
    randomList = []
    numObjects = len(inputList)
    for i in range(numObjects):
        indexSelect = random.randrange(0,len(inputList))
        tempProvider = inputList.pop(indexSelect)
        if (tempProvider.priority == 0):
            randomList.insert(0,tempProvider)
        elif(tempProvider.priority == 1):
            randomList.append(tempProvider)
    return randomList

# populateProviders()
# Inputs:
#   filename : a string with the name of the file containing provider profile information
# Outputs:
#     providerList : a list of scheduler.Provider objects
#
# Reads the provider profile data from an excel file (.xlsx) and populates a list
# of scheduler.Provider objects, then returns this list
def populateProviders(filename):

    provXL = pd.read_excel(filename)
    providerlist = []
    priorityStoI = {"Fixed":0,"Flexible":1}
    for i in range(len(provXL.index)):
        currentRow = provXL.loc[i]
        name = currentRow["First"] + " " + currentRow["Last"]
        spec = currentRow["Specialty"]
        priority = priorityStoI[currentRow["Priority"]]
        # Build empty dayPref array
        dayPref = [[]]
        for n in range(14):
            dayPref.append([])
        # Day preferences are in [ [am location,pm location], ...] format
        # AM Day / Location preferences
        for k in range(14):
            dayPref[k].append(currentRow[5+2*k])
        # PM Day / Location preferences
        for l in range(14):
            dayPref[l].append(currentRow[6+2*l])
        # Total available hours
        shifts = currentRow["Shift Limit"]
        # Construct new object and add to providerlist output
        providerlist.append(sch.Provider(name, spec, dayPref, shifts, priority))

    return providerlist


# populateClinics()
# Inputs:
#   filename : a string with the name of the file containing clinic profile information
# Outputs:
#     clinicList : a list of scheduler.Clinic objects
#
# Reads the clinic profile data from an excel file (.xlsx) and populates a list
# of scheduler.Clinic objects, then returns this list

def populateClinics(filename):
    clinicXL = pd.read_excel(filename)
    clinicList = []
    for i in range(len(clinicXL.index)):
        currentRow = clinicXL.loc[i]
        name = currentRow["Clinic Name"]
        minPed = currentRow[1]
        minAdult = currentRow[2]
        idealPed = currentRow[3]
        idealAdult = currentRow[4]
        maxStaff = currentRow[5]
        clinicList.append(sch.Clinic(name, minPed, minAdult, idealPed, idealAdult, maxStaff))

    return clinicList


# outputClinicSchedule()
# Inputs:
#   clinicList : a list of scheduler.Clinic objects
#   fileName : a string with the target excel file name
#   startDate : a datetime.date object with the starting date of the schedule
# Outputs: None
#
# Overwrites (or creates if it doesn't exist) an excel file with the
# schedule contained in the week attributes of the Clinic objects in clinicList
def outputClinicSchedule(clinicList, fileName, startDate):
    file = open(fileName, "w")
    # In the datetime module, Monday = 0 and Sunday = 6
    weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat", "Sun"]
    colHeaders = []
    colHeaders.append("Day")
    # Column names, 3 slots per clinic per day
    for clinic in clinicList:
        for i in range(3):
            colHeaders.append(clinic.clinic_name + " " + str(i+1))
    # Row labels, each row is a day, label format "Weekday {mo}/{day}"
    dayStrings = []
    for i in range(14):
        tempDay = startDate + datetime.timedelta(days=i)
        dayStrings.append(weekdays[tempDay.weekday()] + " " + str(tempDay.month) +
        "/" + str(tempDay.day) + " AM")
        dayStrings.append(weekdays[tempDay.weekday()] + " " + str(tempDay.month) +
        "/" + str(tempDay.day) + " PM")

    # Create a new DataFrame object to contain the schedule
    schedOut = pd.DataFrame(columns=colHeaders)
    rowCounter = 0;

    for day in range(14):
        for shift in range(2):
            row = []
            row.append(dayStrings[rowCounter])
            for clinic in clinicList:
                for slot in range(3):
                    row.append(clinic.week[day][shift][slot])
            schedOut.loc[rowCounter] = row;
            rowCounter += 1

    schedOutXL = schedOut.set_index('Day', drop=True)
    schedOutXL.to_excel(fileName)
    return;

###
# Test code for outputClinicSchedule()
# This test requires that the scheduler.scheduler() function return the
# list of Clinic objects (Clinic_List) that it modifies

startDate = sch.find_next_monday()
print(startDate)
clinicsIn = populateClinics("Clinic_Template.xlsx")

providersIn = populateProviders("Provider_Preferences.xlsx")
print("\n\nUnrandomized:")
for p in providersIn:
    print(str(p.priority) + " " + p.provider_name)
clinicsOut = sch.scheduler(providersIn, clinicsIn,startDate)
outputClinicSchedule(clinicsOut, "ClinicScheduleTest.xlsx", startDate)

###
# Test code for randomizeList(), read 14 days and read available shifts:
# providersOut = randomizeProviders(providersIn)
# print("\n\nRandomized:")
# for p in providersOut:
#     print(str(p.priority) + " " + p.provider_name + " " + str(p.shifts))
#     print(p.day_preferences)
