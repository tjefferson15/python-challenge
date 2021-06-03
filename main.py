import os 
import csv 
budget_csv = os.path.join ("/Users/tjeff/Desktop/python-challenge/PyBank/Resources/budget_data.csv")

with open(budget_csv,"r") as csvfile:
    csvreader = csv.DictReader (csvfile, delimiter=",")
    totals = []
    for row_count, row in enumerate(csvreader, start=1): 
        value = int(row['Profit/Losses'])
        totals.append(value)

print ("Financial Analysis")
print ("-----------------------")
print ("Total Months: {}".format(row_count))
print ("Total: {}" . format(sum(totals)))
print ("Average Change: ") 
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")

output_file = os.path.join("Analysis.txt") 

with open (output_file, "w") as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("-----------------------\n")
    text_file.write ("Total Months: {}\n".format(row_count))

    