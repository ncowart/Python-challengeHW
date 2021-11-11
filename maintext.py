import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader, None)
    print(header)

    monthly_change = []
    dates = []
    total = []
    profit_loss = []
    total_change = []

    for row in csvreader:
        print(row)
        dates.append(row[0])
        profit_loss.append(row[1])

    total_months = 0
for month in dates:
    total_months += 1

net_total = 0
for row in profit_loss:
    net_total += int(row)

for i in range(1,len(profit_loss)):
    monthly_change.append(float(profit_loss[i])-float(profit_loss[i-1]))
    print(float(profit_loss[i])-float(profit_loss[i-1]))
    print(i)



# print(profit_loss{2})
# print(range(len(profit_loss)))
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_total))
# print(dates)
