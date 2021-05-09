# ************************************************************************
# * This module implements the system's interface with external files.
# *
# *
# * COMPONENT NAME: inout.py
# *
# * VERSION: 3.0 (April 2021)
# *
# * Module Description
# *  This module takes file names and lists of objects from the scheduler module as
# * inputs, and outputs lists of objects. This module creates, reads, and writes .xlsx
# * files.
# * **********************************************************************/

import pandas as pd
import scheduler as sch
import datetime
import random

# This function takes a list of scheduler.Provider objects as inputs and
# returns the objects from the list in a randomized order, with Providers
# whose priority is 0 at the head of the list and 1 at the tail.

def randomizeProviders(inputList):
    randomList = []
    numObjects = len(inputList)
    for i in range(numObjects):
        indexSelect = random.randrange(0, len(inputList))
        tempProvider = inputList.pop(indexSelect)
        if (tempProvider.priority == 0):
            randomList.insert(0, tempProvider)
        elif (tempProvider.priority == 1):
            randomList.append(tempProvider)
    return randomList


# This function reads the provider profile data from an excel file (.xlsx) and
# populates a list of scheduler.Provider objects, then returns this list
def populateProviders(filename):
    provXL = pd.read_excel(filename)
    providerlist = []
    priorityStoI = {"Fixed": 0, "Flexible": 1}
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
            dayPref[k].append(currentRow[5 + 2 * k])
        # PM Day / Location preferences
        for l in range(14):
            dayPref[l].append(currentRow[6 + 2 * l])
        # Total available hours
        shifts = currentRow["Shift Limit"]
        # Construct new object and add to providerlist output
        providerlist.append(sch.Provider(name, spec, dayPref, shifts, priority))

    return providerlist


# This function reads the clinic profile data from an excel file (.xlsx) and
# populates a list of scheduler.Clinic objects, then returns this list.

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


# This function overwrites (or creates if it doesn't exist) an excel file with the
# schedule contained in the week attributes of the Clinic objects in clinicList

def outputClinicSchedule(clinicList, startDate):
    #Create dynamic file name string, create file if it doesn't exist
    fileName = startDate.strftime("%b_%d_%Y_") + "Schedule.xlsx"
    file = open(fileName, "w")
    file.close()

    # In the datetime module, Monday = 0 and Sunday = 6
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    colHeaders = []
    colHeaders.append("Day")
    # Column names, 3 slots per clinic per day
    for clinic in clinicList:
        for i in range(3):
            colHeaders.append(clinic.clinic_name + " " + str(i + 1))
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

    #Iterate through days, shifts, clinics, slots
    for day in range(14):
        for shift in range(2):
            row = []
            row.append(dayStrings[rowCounter])
            for clinic in clinicList:
                for slot in range(3):
                    row.append(clinic.week[day][shift][slot])
            schedOut.loc[rowCounter] = row;
            rowCounter += 1
    # Set the index of the pandas dataframe to be the Day column
    schedOutXL = schedOut.set_index('Day', drop=True)
    # Create an ExcelWriter object and set it to write to the file's first sheet
    writer = pd.ExcelWriter(fileName, engine = 'xlsxwriter')
    schedOutXL.to_excel(writer, sheet_name = 'Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    #Set column widths
    worksheet.set_column('A:J',18)
    #Define formats
    bgGreen = workbook.add_format({'bg_color':'#92D050'})
    bgOrange = workbook.add_format({'bg_color':'#FFC000'})
    bgGray = workbook.add_format({'bg_color':'#BFBFBF'})
    #Set first cell fill colors (Day cells) alternating by 2
    worksheet.conditional_format('A2:A29',
        {'type':'formula',
        'criteria':'=MOD(ROW(),4)<=1',
        'format':bgGreen})

    worksheet.conditional_format('A2:A29',
        {'type':'formula',
        'criteria':'=MOD(ROW(),4)>1',
        'format':bgOrange})
    #Set column header fill colors alternating by 3
    worksheet.conditional_format('B1:J1',
        {'type':'formula',
        'criteria':'=MOD(COLUMN()-2,6)<3',
        'format':bgGray})
    #Save and close file
    writer.save()
    return;
