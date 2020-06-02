import os
import csv
import statistics

# Set a CSV file path
csvpath = os.path.join("Resources_PyBank", "budget_data.csv")


#def pyBank(parameter):

# Reading in the CSV file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)   # Excludes headers

    # Declaration of lists and variables
    dates = []
    profit_losses = []
    changes = []


    for z, row in enumerate(csvreader):
        dates.append(str(row[0]))
        profit_losses.append(int(row[1]))
        if z > 0:
            diffrnc = profit_losses[z] - profit_losses[z-1]
            changes.append(diffrnc)

#------------------------------------------------------------------------------------------

# The total number of months included in the dataset
total_months = len(dates)


# The net total amount of "Profit/Losses" over the entire period
total_amount = sum(profit_losses)


# The average of the changes in "Profit/Losses" over the entire period            
ave_of_changes = round(statistics.mean(changes),2)


# The greatest increase in profits (date and amount) over the entire period
max_value = max(changes)  
indx_max_month = changes.index(max_value) + 1  #find the index of 'the month' that corresponds with 'max_value from changes'
max_month = dates[indx_max_month]


# The greatest decrease in losses (date and amount) over the entire period
min_value = min(changes)
indx_min_month = changes.index(min_value) + 1
min_month = dates[indx_min_month]

#------------------------------------------------------------------------------------------

print(f"Total Months: {total_months}")
print(f"Total Amount: ${total_amount}")
print(f"Average Change: ${ave_of_changes}")
print(f'Greatest Increase in Profits: {max_month} (${max_value})')
print(f'Greatest Decrease In Profits: {min_month} (${min_value})')

#------------------------------------------------------------------------------------------