import os
import csv
#print(os.getcwd)
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

months= []
#total= int
total= 0 
profit_losses= []

with open(csvpath) as csvfile:
    #read header
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        #count months
        months.append(row[0])

        #create array of profit/loss values
        profit_losses.append((int(row[1])))

    change = [profit_losses[i] - profit_losses[i-1] for i in range(1 , len(profit_losses))]
    greatest_increase = max(change)
    greatest_decrease = min(change)
    print(greatest_decrease)

    for row in csvreader:
           if [profit_losses[i] - profit_losses[i-1]== greatest_increase for i in range(1 , len(profit_losses))]:
                greatest_increase_month = str(row[0])
           print(greatest_increase_month)
           months.append(row[0])

        

        #if int(row[i,1]) == greatest_increase:
         #   greatest_increase_month = str(row[0])

    avg_change = sum(change) / len(change)
    number_of_months = len(months)
    total = sum(profit_losses)

    print("yay")

    
exit(0)

'''

        

        

        if int(row[1]) == greatest_decrease:
            greatest_decrease_month = str(row[0])
    
     

    
    

    #Header
    print("Financial Analysis")
    print("---------------------------------------")
    #Total Months
    print("Total Months: " + str(number_of_months))
    #Total
    print("Total: $" + str(total))
    
    
    #Average Change
    print("Average  Change: $" + str(avg_change))
    #Greatest Increase
    print(f"Greatest Increase in Profits: {str(greatest_increase_month)} ( {str(greatest_increase)} )")
    #Greatest Decrease
    print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} ( {str(greatest_decrease)} )")
    print("---------------------------------------")

with open("PyBank_results.txt", "w") as PyBank_results:
    PyBank_results.write(f"""
    Financial Analysis
    ---------------------------------------
    Total Months: {str(len(months))}
    Total: $ {str(total)}
    Average  Change: $ {str(avg_change)}
    Greatest Increase in Profits: {str(greatest_increase_month)} ( {str(greatest_increase)} )
    print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} ( {str(greatest_decrease)} )
    ---------------------------------------""")
  '''  