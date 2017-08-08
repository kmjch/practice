import csv
import sys

# For Mac OS X, save your CSV file in "Windows Comma Separated (.csv)" format.

filename = sys.argv[1]

with open(filename, 'rU') as csvfile:
#     filereader = csv.DictReader(csvfile)
#     for row in filereader:
#         print row['Organization'], row['Willing to donate']

    org_info_dict = {}
    filereader = csv.reader(csvfile)
    for org, amount in filereader:
        org_info_dict[org] = amount
    print org_info_dict
