import csv

EMPLOYEE_FILE = 'EmployeePay.csv'

infile = open(EMPLOYEE_FILE, 'r', newline='')

reader = csv.reader(infile, delimiter=',')

field_name = next(reader)

for row in reader:
    empid = row[0]
    empfname = row[1]
    emplname = row[2]
    salary = row[3]
    bonus = row[4]

    print(empid, empfname, emplname, salary, bonus)
