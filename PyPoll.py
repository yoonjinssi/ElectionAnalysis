# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recevied votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# file_to_load ='Resources/election_results.csv'
# election_data = open(file_to_load, 'r')
# election_data.close()

# file_to_load = 'Resources/election_results.csv'
# election_data = open(file_to_load, 'r')
# election_data.close()

# with open(file_to_load) as election_data:
#     print(election_data)
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 

candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            # Add that candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin counting that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count ---> I don't understand this part. How putthing this aligned with if counts every candidate
        candidate_votes[candidate_name] += 1

        # Determne the % of votes for each candidate by looping through the counts.
        #1.Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2.Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes)*100
        #4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.") 
        
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate =candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    
# Print the candidate list.
    
    print(winning_candidate_summary)

# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # open(file_to_save, "w")
# outfile = open(file_to_save, "w")
# outfile.write("Hello World")
# outfile.close()

# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("---------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# Read the file object with the reader function.

# Print each row in the CSV file.
    
