import os
import csv

# Set a CSV file path
csvpath = os.path.join("Resources_PyPoll", "election_data.csv")

# Reading in the CSV file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)   # Excludes headers

    # Declaration of lists and variables
    all_votes = []
    unique_candidates = []

    for z, row in enumerate(csvreader):
        all_votes.append(row[2])


# The total number of votes cast
total_votes = len(all_votes)

# A complete list of candidates who received votes (uniques from Candidate column)
if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

