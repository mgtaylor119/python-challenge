import os
import csv
csv_file = os.path.join("Resources", "budget_data.csv")

total = 0
column_name = 'Profit/Losses'
column1 = 'Date'
monthcounter = 0
store_diff=[]
holder = 0
change = 0
greatest_increase = 0
greatest_decrease = 0
i=0

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
#iterates through file to capture count of months and identify the difference of profit/losses between month and prior month:
    for row in reader:
        value = float(row[column_name])
        month = row[column1]
        total += value
        monthcounter = monthcounter + 1
        if holder != value:
            change = value - holder
            if change != value:
                store_diff.append(change)
#this code block finds the greatest increase/decrease: 
        if monthcounter > 1 and store_diff[i] > greatest_increase:
            greatest_increase = store_diff[i]
            increase_month = month
            i=i+1
        elif monthcounter > 1 and store_diff[i] < greatest_decrease:
            greatest_decrease = store_diff[i]
            decrease_month = month
            i=i+1
        elif monthcounter >1:
            i=i+1   
        
        holder = value
result = int(total)

sum = sum(store_diff)
average_change = round(sum/(monthcounter - 1),2)
greatest_increase = round(greatest_increase)
greatest_decrease = round(greatest_decrease)

# prints to terminal:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthcounter}")
print(f"Total: ${result}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# creates and writes to text file:
txt_file = os.path.join("Analysis", "results.txt")
with open(txt_file, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {monthcounter}\n")
    f.write(f"Total: ${result}\n")
    f.write(f"Average Change: ${average_change}\n")
    f.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")