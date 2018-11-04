import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #get the header
    header = next(csvreader)
    #add a new column called change
    header.append('change')

    totalMonths = 0
    total_net_amount = 0

    rows = []
    for i, row in enumerate(csvreader):
        totalMonths += 1
        total_net_amount += int(row[header.index('Profit/Losses')])
        #adding a default 0 value for the column change
        row.append(0)
        rows.append(row)

    for x in range(len(rows)):
        if x > 0:
            #calculating the value for change in each row, except the first row
            rows[x][header.index('change')] = int(rows[x][header.index('Profit/Losses')]) - int(rows[x-1][header.index('Profit/Losses')])

#use comprehension to get the sum of change, and the divisor being the total row count of rows other than the first row
sum_changes, total_changes = sum([row[header.index('change')] for i, row in enumerate(rows) if i > 0]), i
#get the row with the greatest increase in profits
most_profitable = max(rows, key=lambda item: item[2])
#get the row with greatest decrease in losses
worst_loss = min(rows,key=lambda item: item[2])

#prep output
output = []
output.append('Financial Analysis')
output.append('-' * 50)
output.append(f'Total Months: {totalMonths}')
output.append(f'Total: ${total_net_amount}')
output.append(f"Average  Change: ${round(sum_changes/total_changes, 2)}")
output.append(f"Greatest Increase in Profits: {most_profitable[header.index('Date')]} (${most_profitable[header.index('change')]})")
output.append(f"Greatest Decrease in Profits: {worst_loss[header.index('Date')]} (${worst_loss[header.index('change')]})")

outputfile = os.path.join('.', 'Resources', 'output.dat')

with open(outputfile, mode='wt', encoding='utf-8') as f:
    for line in output:
        f.write(line + '\n')
        print(line)