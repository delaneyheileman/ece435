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
        clPref = []
        # Build empty dayPref array
        dayPref = [[]]
        for n in range(7):
            dayPref.append([])
        daysOff = [0] * 7
        # for j in range(3):
        #     clPref.append(currentRow[18+j])
        # Day preferences are in [ [am,pm], [am,pm] ...] format
        # AM Day / Location preferences
        for k in range(7):
            dayPref[k].append(currentRow[3+2*k])
        # PM Day preferences
        for l in range(7):
            dayPref[l].append(currentRow[4+2*l])
            # If both am and pm preference is 0, flag this as a day off
            # if (dayPref[l][0] == ) & (dayPref[l][1] == 0):
            #     daysOff[l] = 1
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

clinic_filename = "Clinic_Template.xlsx"
cl = populateClinics(clinic_filename)

for i in range(3):
    print(cl[i].clinic_name, cl[i].min_ped, cl[i].min_aud, cl[i].idl_ped, cl[i].idl_aud, cl[i].max_staff)



## The code below tests the populateProviders function and prints the objects to the terminal
prov_filename = "Provider_Template.xlsx"
pl = populateProviders(prov_filename)

for i in range(12):
    print(f'{pl[i].provider_name}, {pl[i].specialty},{pl[i].day_preferences}, {pl[i].total_available_hours}')


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
