import csv

CUSTFILE = 'customers.csv'
CUST_COUNTRY_FILE = 'customer_country.py'

# open customers csv file
infile = open(CUSTFILE, 'r', newline='')
outfile = open(CUST_COUNTRY_FILE, 'w', newline='')

# create csv object
reader = csv.reader(infile, delimiter=',')
writer = csv.writer(outfile, delimiter=',')

# skip field row
field_name = next(reader)

# label row
for row in reader:
    customer_id = row[0]
    firstname = row[1]
    lastname = row[2]
    city = row[3]
    country = row[4]
    phone = row[5]

# loop through reader
cust_country = [firstname, lastname, country]
writer.writerow(cust_country)

infile.close()
outfile.close()
