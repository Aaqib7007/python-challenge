import csv
import os

# File path for the input CSV
csvpath = os.path.join("Resources", "election_data.csv")

#File path for the output CSV
output_file = os.path.join("analysis", "election_results")

# Initialize variables
row_count = 0
candidate_votes = {}

if os.path.exists(csvpath):
    with open(csvpath, "r", newline="") as csvfile:
        # Use DictReader to read the CSV file
        reader = csv.DictReader(csvfile)

        # Iterate over each row
        for row in reader:
            row_count += 1
            candidate = row["Candidate"]

            # Count votes for each candidate
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    # Calculate the percentage of votes each candidate won
    candidate_percentages = {candidate: (votes / row_count) * 100 for candidate, votes in candidate_votes.items()}
    candidate_list = sorted(candidate_votes.keys())

    # Determine the winner based on the popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

   # Prepare the results for output
    results = []
    results.append("Election Results")
    results.append("-------------------------")
    results.append(f"Total Votes: {row_count}")
    results.append("-------------------------")
    results.append(f"List of Candidates who received votes: {candidate_list}")
    results.append("-------------------------")
    for candidate in candidate_list:
        results.append(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
    results.append("-------------------------")
    results.append(f"Winner: {winner}")
    results.append("-------------------------")

    # Write the results to the text file
    with open(output_file, "w") as txtfile:
        for line in results:
            txtfile.write(line + "\n")

    # Print the results to the terminal
    for line in results:
        print(line)

else:
    print(f"The file {csvpath} does not exist.")

