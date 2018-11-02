import sys

def read_file(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        #read the header, and convert to a list of columns
        header = f.readline()[:-1] #ignore the \n at the end of the line
        columns = header.split(',')
        #adding a new column for the change
        columns.append('change')

        #converting each line as a row list and adding the new column for change
        lines = [line[:-1] for line in f.readlines()]
        rows = []
        for x in range(len(lines)):
            row = lines[x].split(',')
            row.append('0')
            rows.append(row)
            if x > 0:
                rows[x][2] = str(int(rows[x][1]) - int(rows[x-1][1]))
        #return the lists of columns and rows
        return columns, rows

def output_results(filename, total_months, total_net_amount, total_change_in_proft_loss, max_increase_in_profit_month, max_increase_in_profit, max_decrease_in_profit_month, max_decrease_in_profit):
    output = []
    output.append("Financial Analysis")
    output.append("-" * 50)
    output.append(f"Total Months: {total_months}")
    output.append(f"Total: ${total_net_amount}")
    output.append(f"Average Change: ${round(total_change_in_proft_loss/(total_months - 1), 2)}")
    output.append(f"Greatest Increase in Profits: {max_increase_in_profit_month} (${max_increase_in_profit})")
    output.append(f"Greatest Decrease in Profits: {max_decrease_in_profit_month} (${max_decrease_in_profit})")

    with open(filename, mode='wt', encoding='utf-8') as f:
        for line in output:
            f.write(line + '\n')
            print(line)
    
def main(input_filename, output_filename):
    columns, rows = read_file(input_filename)
    total_net_amount = 0
    total_change_in_proft_loss = 0
    max_increase_in_profit = 0
    max_increase_in_profit_month = ''
    max_decrease_in_profit = 0
    max_decrease_in_profit_month = ''

    for x in range(len(rows)):
        total_net_amount += int(rows[x][columns.index('Profit/Losses')])
        total_change_in_proft_loss += int(rows[x][columns.index('change')])
        if max_increase_in_profit < int(rows[x][columns.index('change')]):
            max_increase_in_profit_month = rows[x][columns.index('Date')]
            max_increase_in_profit = int(rows[x][columns.index('change')])
        if max_decrease_in_profit > int(rows[x][columns.index('change')]):
            max_decrease_in_profit_month = rows[x][columns.index('Date')]
            max_decrease_in_profit = int(rows[x][columns.index('change')])
    output_results(output_filename, x + 1, total_net_amount, total_change_in_proft_loss, max_increase_in_profit_month, max_increase_in_profit, max_decrease_in_profit_month, max_decrease_in_profit)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])