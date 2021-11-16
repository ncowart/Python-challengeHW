# Dependencies 
import csv 
import os 

# Define variables for final output 
vote_total = 0
candidates = []
percents = []
vote_counts = []
winner = ""

# Define function to properly output results
def printOutput():
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {vote_total}")
    print("-----------------------------")
    i = 0
    for candidate in candidates:
        print(f"{candidate}: {percents[i]}% ({vote_counts[i]})")
        i = i + 1
    print("-----------------------------")
    print(f"Winner: {winner}")
    print("-----------------------------")

# Define csv_path
csv_path = os.path.join('pyPoll', 'Resources','election_data.csv')

# Open csv_path as cvsfile
with open(csv_path) as csvfile: 
     # Create csvreader object and pass headers
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    # Iterate through file and acquire 
    for row in csvreader:
        vote_total = vote_total + 1
        i = candidates.index(row[2]) if row[2] in candidates else None
        if i == None: 
            candidates.append(row[2])
            vote_counts.append(1)
        else: 
            vote_counts[i] = vote_counts[i] + 1
    csvfile.close()

# Add percentages
for count in vote_counts:
    percent = round(count/vote_total * 100, 2)
    percents.append(percent)

# Find winner
maxVotes = max(vote_counts)
i = vote_counts.index(maxVotes)
winner = candidates[i]

# Write to txt file
with open('pyPoll/output.txt', 'w+') as fileout: 
    fileout.write("Election Results\n")
    fileout.write("-----------------------------\n")
    fileout.write(f"Total Votes: {vote_total}\n")
    fileout.write("-----------------------------\n")
    i = 0
    for candidate in candidates:
        fileout.write(f"{candidate}: {percents[i]}% ({vote_counts[i]})\n")
        i = i + 1
    fileout.write("-----------------------------\n")
    fileout.write(f"Winner: {winner}\n")
    fileout.write("-----------------------------\n")
    
# Print final output
printOutput()
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
