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


        # The total number of votes cast
        total_votes = len(votes_casted)


        # A complete list of candidates who received votes (uniques from Candidate column)
        if row[2] not in unique_candidates:
            
            unique_candidates.append(row[2])
            

    # The total number of votes and The percentage of votes each candidate won
    for candidate in unique_candidates:
            candidate_count.append(votes_casted.count(candidate))
            percent.append(round(votes_casted.count(candidate)/total_votes*100, 3))


# The winner of the election based on popular vote
max_votes= max(candidate_count)  
indx_winner = candidate_count.index(max_votes)  
winner = unique_candidates[indx_winner]
            


print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------")

for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {percent[i]}% ({candidate_count[i]})")

print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")


#------------------------------------------------------------------------------------------




