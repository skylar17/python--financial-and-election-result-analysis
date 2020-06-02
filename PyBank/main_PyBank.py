import os
import csv
import statistics

# Set CSV file path
csvpath = os.path.join("Resources_PyBank", "budget_data.csv")


#def pyBank(parameter):

# Reading data of CSV file excluding headers
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # Declaration of lists and variables
    months = []
    profit_losses = []
    changes = []


    for row in csvreader:

        months.append(str(row[0]))
        profit_losses.append(int(row[1]))
                
        # Counting The total number of months
        x = len(months)

        # Counting The net total amount of "Profit/Losses"
        y = sum(profit_losses)

        # Calculating The average of the changes in "Profit/Losses"
        for z in range(1, len(profit_losses)):
            diffrnc = profit_losses[z] - profit_losses[z-1]
            changes.append(diffrnc)
            
            AveOfChanges = round(sum(changes) / len(changes),2)


    print(f"Total Months: {x}")
    print(f"Total Amount: {y}")
    print(f"Average Change: ${AveOfChanges}")
    


#----------------------------------------------------------------------------

