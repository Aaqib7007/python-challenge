import os
import csv

# File path for the input CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

# File path for the output CSV
output_file = os.path.join("analysis", "financial_analysis_output.txt")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_value = None
changes = []
greatest_increase = {"date": None, "amount": 0}  # Start with 0
greatest_decrease = {"date": None, "amount": 0}    # Start with 0

# Open and read the CSV file
with open(csvpath, mode='r') as file:
    csvreader = csv.reader(file)
    
    # First row is the header
    header = next(csvreader) 

    # Initialize variables for the first comparison
    first_row = True
    
    # Loop through the rows to calculate totals and changes
    for row in csvreader:
        # Extract the current "Profit/Losses" value from the second column
        current_value = int(row[1])
        
        # Update total months and total profits/losses
        total_months += 1
        total_profit_losses += current_value
        
        # Calculate the change from the previous month if this is not the first row
        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)
            
            # Initialize greatest increase and decrease based on the first change
            if first_row:
                greatest_increase["amount"] = change
                greatest_decrease["amount"] = change
                greatest_increase["date"] = row[0]
                greatest_decrease["date"] = row[0]
                first_row = False
            
            # Check if this change is the greatest increase so far
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row[0]  # Assuming the date is in the first column, index 0

            # Check if this change is the greatest decrease so far
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row[0]  # Assuming the date is in the first column, index 0
        
        # Update the previous value to the current one for the next iteration
        previous_value = current_value

# Calculate the average change in "Profit/Losses"
average_change = sum(changes) / len(changes) if changes else 0

# Format the results
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the output to the terminal
print(output)

# Export the results to a text file
with open(output_file, "w", newline='') as datafile:
    datafile.write(output)
