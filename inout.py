import csv

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
with open('test - Sheet1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works is {row[1]} old and {row[2]} this tall.')
            myName = {row[0]}
            print(f'\t Name is {myName}')
            line_count += 1
    print(f'processed {line_count} lines.')
