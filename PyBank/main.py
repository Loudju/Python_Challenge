#Dependencies
import csv

#Files to load and output
budget_data = "PyBank/Resources/budget_data (1).csv"
Analysis_output = "PyBank/Analysis.txt"

#Track these revenue parameters
total_months = 0
previous_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_revenue = 0

#Read csv and convert to list of dictionaries
with open(budget_data) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        #Get totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Get the revenue change
        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        #Calculate the greatest increase 
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change 
    
        #Calculate the greatest decrease 
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

 #Calculate the average revenue change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


 #Generate Output Analysis     
Analysis_output = (
     f"\nFinancial Analysis\n"
     f"---------------------------\n"
     f"Total Months: {total_months}\n"
     f"Total Revenue: ${total_revenue}\n"
     f"Average Revenue Change: ${revenue_avg}\n"
     f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
     f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"  
 )     

#Print Output
print(Analysis_output)

 #Export results to a beautiful text file
with open(Analysis_output, "w") as txt_file:
     txt_file.write(Analysis_output)
    
