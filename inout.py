#last UD 4/11/21 4:39 pm
import pandas as pd
import scheduler as sch

## Given the file name (.xlsx) where provider profiles are stored,
## returns a list of provider objects
def populateProviders(filename):

    provXL = pd.read_excel(filename)
    providerlist = []
    for i in range(len(provXL.index)):
        currentRow = provXL.loc[i]
        name = currentRow["First"] + " " + currentRow["Last"]
        spec = currentRow[2]
        # Build empty dayPref array
        dayPref = [[]]
        for n in range(7):
            dayPref.append([])
        # Day preferences are in [ [am location,pm location], ...] format
        # AM Day / Location preferences
        for k in range(7):
            dayPref[k].append(currentRow[3+2*k])
        # PM Day / Location preferences
        for l in range(7):
            dayPref[l].append(currentRow[4+2*l])
        # Total available hours
        availHours = currentRow["Hour Limit"]
        # Construct new object and add to providerlist output
        providerlist.append(sch.Provider(name, spec, dayPref, availHours))

    return providerlist

def populateClinics(filename):
    clinicXL = pd.read_excel(filename)
    cliniclist = []
    for i in range(len(clinicXL.index)):
        currentRow = clinicXL.loc[i]
        name = currentRow["Clinic Name"]
        minPed = currentRow[1]
        minAdult = currentRow[2]
        idealPed = currentRow[3]
        idealAdult = currentRow[4]
        maxStaff = currentRow[5]
        cliniclist.append(sch.Clinic(name, minPed, minAdult, idealPed, idealAdult, maxStaff))

    return cliniclist
