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
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        print(row)


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
    
