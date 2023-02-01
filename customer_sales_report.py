import csv

SALESFILE = 'sales.csv'
SALES_REPORT_FILE = 'salesreport.csv'

# open customers csv file
infile = open(SALESFILE, 'r', newline='')
outfile = open(SALES_REPORT_FILE, 'w', newline='')

# create csv object
reader = csv.reader(infile, delimiter=',')
writer = csv.writer(outfile, delimiter=',')

# skip field row
field_name = next(reader)


CustomerID = '250'
cust_total = 0

# label row

for row in reader:

    if CustomerID != row[0]:
        outfile.write(CustomerID + ',' + format(cust_total, '.2f') + '\n')
        cust_total = 0
        CustomerID = row[0]
    SubTotal = float(row[3])
    TaxAmt = float(row[4])
    Freight = float(row[5])
    total = SubTotal + TaxAmt + Freight
    cust_total += total
