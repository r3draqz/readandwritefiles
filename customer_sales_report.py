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


CustomerID = 0
gtotal = 0

# label row

for row in reader:
    # OrderDate = row[1]
    # ShipDate = row[2]
    SubTotal = float(row[3])
    TaxAmt = float(row[4])
    Freight = float(row[5])
    sales_report = [CustomerID, gtotal]

    Total = SubTotal + TaxAmt + Freight
    # if int(row[0]) == CustomerID:

    # gtotal += Total
    # sales_report = [CustomerID, gtotal]
    # writer.writerow(sales_report)
    # CustomerID += 1

    if CustomerID != row[0]:
        writer.writerow(sales_report)
        Total = 0
        CustomerID = row[0]

    gtotal += Total
'''  
    if int(row[0]) != CustomerID:

        sales_report = [CustomerID, gtotal]
        writer.writerow(sales_report)
        gtotal = Total
        CustomerID += 1

    Total = SubTotal + TaxAmt + Freight
'''

# Total = 0
