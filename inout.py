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
        spec = currentRow["Specialty"]
        amPref = []
        pmPref = []
        clPref = []
        daysOff = [0] * 7
        # Day preferences will be in a [ [am,pm], [am,pm] ...] format, this needs to be updated
        for j in range(3):
            clPref.append(currentRow[18+j])
        for k in range(7):
            amPref.append(currentRow[4+2*k])
        for l in range(7):
            pmPref.append(currentRow[5+2*l])
            # If both am and pm preference is 0, flag this as a day off
            if (pmPref[l] == 0) & (amPref[l] == 0):
                daysOff[l] = 1

        availHours = currentRow["Hour Limit"]
        providerlist.append(sch.Provider(name, spec, clPref, amPref, pmPref, daysOff, availHours))

    return providerlist


## The code below tests the populateProviders function and prints the objects to the terminal
prov_filename = "Provider_Template.xlsx"
pl = populateProviders(prov_filename)

for i in range(3):
    print(pl[i].provider_name, pl[i].specialty,pl[i].am_day_preferences, pl[i].pm_day_preferences, pl[i].days_off, pl[i].clinic_preference)


# import csv
#below was a class I was just using for testing
#class myProvider:
#    id = 0
#    name = ""
#    dayPref = []
#
#    def __init__(self, id, name, dayPref):
#        self.id = id
#        self.name = name
#        self.dayPref = dayPref
#        self.all = "id + name + dayPref"
#
#    def testFunc(self):
#        print("Hello here is my info:" + self.all)

#code to open a CSV. This was just my test version and it will need to be changed
#a lot for the assignment. Uses a dumby csv I made for this
# with open('test - Sheet1.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {",".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works is {row[1]} old and {row[2]} this tall.')
#             myName = {row[0]}
#             print(f'\t Name is {myName}')
#             line_count += 1
#     print(f'processed {line_count} lines.')
