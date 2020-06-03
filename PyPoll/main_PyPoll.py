import os
import csv

# Set a CSV file path
csvpath = os.path.join("PyPoll", "Resources_PyPoll", "election_data.csv")

# Reading in the CSV file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)   # Excludes headers

    # Declaration of lists and variables
    votes_casted = []
    unique_candidates = []
    candidate_count = []
    percent = []

    for z, row in enumerate(csvreader):
        votes_casted.append(row[2])

    
        # A complete list of candidates who received votes (uniques from Candidate column)
        if row[2] not in unique_candidates:
            
            unique_candidates.append(row[2])
            #x = len(unique_candidates)
            #print(f"{x}")

# The total number of votes cast
total_votes = len(votes_casted)


    # for candidate in unique_candidates:
    #         candidate_count.append(votes_casted.count(candidate))
    #         percent.append(round(votes_casted.count(candidate)/total_votes*100,3))


print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------")




