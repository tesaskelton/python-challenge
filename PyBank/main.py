import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

 # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    num_months = 0
    total = 0
    change = 0
    change_array = []
    prev_pl =0
    increase = 0
    decrease = 0
    counter = 0

    # Read through each row of data after the header
    for row in csv_reader:

        # Count Months
        
        #if row[0] != row[i+1]:
        #print(row)
        num_months += 1
        total += int(row[1])

        if counter > 0:
          change = int(row[1]) - prev_pl
          change_array.append(change)
        
        counter += 1
        prev_pl = int(row[1])

        if change > increase:
            increase = change
            inc_month = row[0]
        elif change < decrease:
            decrease = change
            dec_month = row[0]
        
       
    
    f= open("PyBank_results.txt", 'w')
    f.write ('Total Months: ' + str(num_months) + '\n')
    print ('Total Months: ' + str(num_months))
    f.write ('Total: ' + str(total) + '\n')
    print ('Total: ' + str(total))
    f.write ('Average Change: ' + str(sum(change_array)/len(change_array)) + '\n')
    print ('Average Change: ' + str(sum(change_array)/len(change_array)))
    f.write ('Greatest Increase in Profit: ' + str(increase) + ' ' + inc_month + '\n')
    print ('Greatest Increase in Profit: ' + str(increase) + ' ' + inc_month)
    f.write ('Greatest Decrease in Profit: ' + str(decrease) + ' ' + dec_month + '\n')
    print ('Greatest Decrease in Profit: ' + str(decrease) + ' ' + dec_month)
    f.close()
