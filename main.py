import os
import csv

csvreader = os.path.join("election_data.csv")

with open(csvreader) as csvfile:
    election_data = csv.reader(csvfile, delimiter =',')
    header = next(csvreader, None)
    print(header)

votes_counted = []
candidates = []
total_votes = []
election_data = []

for row in csvreader:
    print(row)
    candidates.append(row[2])


    votes_counted += 1
    candidates[row[2]] = candidates.get(row[2],0) + 1
    print(row)