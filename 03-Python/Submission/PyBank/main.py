
import os
import csv
import numpy as np


total_months = 0
total_profits =0
changes =[]
date_count = []
max_change = 0
greatest_inc_month = 0
min_change = 0
greatest_dec_month = 0


csvpath = os.path.join("Resources\\budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)
    row = next(csvreader)

    previous_profit = int(row[1])
    total_months = total_months + 1
    total_profits = total_profits + int(row[1])
    max_change = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
            total_months = total_months + 1
            total_profits = total_profits + int(row[1])

    
            change = int(row[1]) - previous_profit
            changes.append(change)
            previous_profit = int(row[1])
            date_count.append(row[0])
        
     
            if int(row[1]) > max_change:
                max_change = int(row[1])
                greatest_inc_month = row[0]
            
 
            if int(row[1]) < min_change:
                min_change = int(row[1])
                greatest_dec_month = row[0]  
    average_change = sum(changes)/len(changes)
    high = max(changes)
    low = min(changes)

 #print to terminal   
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_profits))
    print(average_change)
    print(greatest_inc_month, max(changes))
    print(greatest_dec_month, min(changes))


output_path = "PyBank.txt"
with open(output_path, "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------------------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total_profits}\n")
    text.write(f"Average Change: ${average_change}\n")
    text.write(f"Greatest Increase in Profits: {greatest_inc_month} (${max_change})\n")
    text.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${min_change})\n")   


