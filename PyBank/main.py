import os
import csv
#print(os.getcwd)
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

months=[]
total= int
total= 0 
profit_losses=[]
change=[]

with open(csvpath) as csvfile:
    #read header
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #put first entries in month and profit_losses lists
    csv_firstrow = next(csvreader)
    months.append(str(csv_firstrow[0]))
    profit_losses.append(int(csv_firstrow[1]))

    
    
    for row in csvreader:
        
        #add to list of months
        months.append(row[0])

        #add to list of daily change values
        change.append((int(row[1])) - profit_losses[-1])

        #add to list of profit/loss values
        profit_losses.append((int(row[1])))

        #define greatest increase and decrease
        greatest_increase = max(change)
        greatest_decrease = min(change)

        #determine greatest increase and decrease as well as corresponding month in which it occured
        if change[-1] == greatest_increase:
            greatest_increase_month = str(row[0])

        if change[-1] == greatest_decrease:
            greatest_decrease_month = str(row[0])
        
    #CHECKING WORK
    """    
    print(f"CHANGE:                         {change}")
    print(f"MONTHS:                         {months}")
    print(f"Profit Losses:                  {profit_losses}")
    print(greatest_increase_month)
    print(greatest_decrease_month)
    """
    #calculate average change and total
    avg_change = sum(change) / len(change)
    total = sum(profit_losses)

    #Header
    print("Financial Analysis")
    print("---------------------------------------")
    #Total Months
    print("Total Months: " + str(len(months)))
    #Total
    print("Total: $" + str(total))
    #Average Change
    print(f"Average  Change: $ {str(round(avg_change,2))}")
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
    Average  Change: $ {str(round(avg_change,2))}
    Greatest Increase in Profits: {str(greatest_increase_month)} ( {str(greatest_increase)} )
    Greatest Decrease in Profits: {str(greatest_decrease_month)} ( {str(greatest_decrease)} )
    ---------------------------------------""")
