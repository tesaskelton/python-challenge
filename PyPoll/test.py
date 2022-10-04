import os
import csv

polldata_csv = os.path.join("Resources", "election_data.csv")

csv_reader = csv.DictReader(polldata_csv, skipinitialspace=True)
# Open and read csv
#with open(polldata_csv) as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter = ",")

 # Read the header row first (skip this part if there is no header)
    #csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

col = []
for i in csv_reader:
        col.append(i[Candidate])

    # all items in the column...
    #print(col)
# only unique items in the column...
print(list(set(col)))