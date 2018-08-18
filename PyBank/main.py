

import os
import csv

total_months = 0
total = 0

change = []
month = []
prev_row_values = 0

#tells what file we're working on. Need to look up what the os.path.join means
input_file = os.path.join('..', 'Resources', 'budget_data.csv')

#Open, then skip the first line. Next time I would name the csv reader pybankwork. 
#wasn't sure what I was doing while watching the video
with open (input_file, newline = '' ) as pybankwork:
    csv_reader = csv.reader(pybankwork, delimiter = ',')
    next(csv_reader)
    
    #Loop through each row
    for row in csv_reader:
        #for output later
        total_months = total_months + 1
        #Add up the total for all of the second column
        total = total + int(row[1])
        #need a value to poulate change list .  
        rev_diff = int(row[1]) - prev_row_values
        #jump the value down for the next change calc
        prev_row_values = int(row[1])
        #Store Values in lists for use later
        change = change + [rev_diff]
        month = month + [row[0]]
    
    #going to need these for terminal output later
    greatest_change = max(change)
    greatest_loss = min(change)
    avg_change = sum(change)/len(change)
    #trying to take the index of the max value in the list change which 
    #should be populated and use that value to grab the value at the 
    #same index in the list "month" 
    month_great_change = change.index(max(change))
    month_great_loss = change.index(min(change))
    greatest_change_month = str([month.index(month_great_change)])
    greatest_loss_month = str(month.index(month_great_loss))

 

print(f"")
print(f"")
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total}")
print(f"{avg_change}")
print(f"{greatest_change_month}" + f"${greatest_change}")
print(f"{greatest_loss_month}" + f"${greatest_loss}")

output_path = os.path.join('..', 'PyOut', 'bank_analysis.csv')
with open (output_path,  "w", newline = "") as datafile:
    writer = csv.writer(datafile, delimiter=',')
    writer.writerows()  