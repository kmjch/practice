import csv
import sys

# For Mac OS X, save your CSV file in "Windows Comma Separated (.csv)" format.

headers = sys.argv[1:]

with open("new_file.csv", 'wb') as csvfile:
#     filereader = csv.DictReader(csvfile)
#     for row in filereader:
#         print row['Organization'], row['Willing to donate']

    filewriter = csv.writer(csvfile, dialect='excel')
    filewriter.writerow(headers)
