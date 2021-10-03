#Your task is to create a Python script that analyzes the records to calculate each of the following:
#import dependencies
import os
#import module for reading CSV Files
import csv
#specify file path
FilePath = os.path.join('Resources', 'budget_data.csv')
# Declare variables for Months, Profit Loss
total_months = 0
month_of_change = []
profit_loss = 0
past_profit_loss = 0
profit_loss_change = 0
greatest_increase = ['',0]
greatest_decrease = ['', 99999999]
total_profit_loss_changes = []

#open file
with open(FilePath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Skip Header
    header = next(csvreader)   
    first_row = next(csvreader)
    total_months = total_months + 1
    profit_loss = profit_loss + int(first_row[1])
    past_profit_loss = int(first_row[1])
    print(f'CSV Header: {header}')
    for row in csvreader:
        total_months = total_months + 1
        profit_loss = profit_loss + int(first_row[1])
        profit_loss_change = int(row[1]) - past_profit_loss
        past_profit_loss = int(row[1])
        total_profit_loss_changes = total_profit_loss_changes + [profit_loss]
        month_of_change = month_of_change + [row[0]]

        if profit_loss > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss       
        if profit_loss < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss 
profit_loss_average = round(sum(total_profit_loss_changes)/len(total_profit_loss_changes), 2)

       
       
#Print
print('Financial Analysis')
print('-------------------')
print(f'Total Months:{total_months}')
print(f'Total: ${profit_loss}')
print(f'Average Change: ${profit_loss_average}')
print(f'Greatest Increase in Profits:' + str(greatest_increase[0]) + ' ($' + str(greatest_increase[1]) + ')')
print(f'Greatest Decrease in Profits:' + str(greatest_decrease[0]) + ' ($' + str(greatest_decrease[1]) + ')')

#write csv to test
#Text File path
txt_file = os.path.join('Resources', 'PyBankTXT')
with open('txt_file', "w") as text:
    text.write('Financial Analysis')
    text.write('\n')
    text.write('-----------------')
    text.write('\n')
    text.write(f'Total Months:{total_months}')
    text.write('\n')
    text.write(f'Total: ${profit_loss}')
    text.write('\n')
    text.write(f'Average Change: ${profit_loss_average}')
    text.write('\n')
    text.write(f'Greatest Increase in Profits:' + str(greatest_increase[0]) + ' ($' + str(greatest_increase[1]) + ')')
    text.write('\n')
    text.write(f'Greatest Decrease in Profits:' + str(greatest_decrease[0]) + ' ($' + str(greatest_decrease[1]) + ')')

