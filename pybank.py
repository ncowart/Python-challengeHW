# Import os and csv modules
import os 
import csv

# Define variables needed to collect from dataset
month_num = 0
profit_loss = 0
average_change = 0
greatest_month = ""
greatest_increase = 0
lowest_month = ""
greatest_decrease = 0

# Define function to print out results correctly
def printOutput():
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {month_num}")
    print(f"Total: ${profit_loss}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})")
    return


# Create csv path variable 

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Open CSV file in with variable assignment

with open(csvpath) as csvfile:

    # Define variables to store current and las month and profit/loss and changes list variable for calculating average at end
    currentMonth = ""
    lastMonth = ""
    currentProfit = 0
    lastProfit = 0
    changes = []
    # Create csvreader variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Grab headers and procedd past the line
    csv_header = next(csvreader)

     # Loop through csvreader and start to fill missing variable
    for row in csvreader:

        # If else to handle first month
        if lastMonth == "":
            lastMonth = row[0]
            lastProfit = row[1]
            currentMonth = row[0]
            currentProfit = row[1]
        else:
            currentMonth = row[0]
            currentProfit = row[1]
            change = int(currentProfit) - int(lastProfit)
            changes.append(change)
            if change > greatest_increase:
                greatest_increase = change
                greatest_month = row[0]
            if change < greatest_decrease: 
                greatest_decrease = change
                lowest_month = row[0]
            profit_loss = int(profit_loss) + int(currentProfit)

        month_num = month_num + 1
        
csvfile.close()
# Loop through changes to get total the divide by length of list for average. Round to 2 decimal places
total = 0
for change in changes:
    total = total + change
average_change = round(total/len(changes),2)

# Save as text file
with open("pyBank/output.txt", 'w+') as fileout: 
    fileout.write("Financial Analysis\n")
    fileout.write("----------------------------------\n")
    fileout.write(f"Total Months: {month_num}\n")
    fileout.write(f"Total: ${profit_loss}\n")
    fileout.write(f"Average Change: ${average_change}\n")
    fileout.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n")
    fileout.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease})\n")
    fileout.close()

# Use printOutput to print final results
printOutput()
    