import os
import csv

banner_length = 25

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #get the header
    header = next(csvreader)
    #read the rest of the file
    rows = [line for line in csvreader]

#A complete list of candidates who received votes
candidates = set([row[header.index('Candidate')] for row in rows])
#The total number of votes cast
total_votes = len(rows)
results = []
for candidate in candidates:
    result = []
    result.append(candidate)
    #The total number of votes each candidate won
    total_votes_per_candidate = len([row for row in rows if row[header.index('Candidate')] == candidate])
    #The percentage of votes each candidate won
    result.append(total_votes_per_candidate/total_votes)
    result.append(total_votes_per_candidate)
    results.append(result)
#sort the results by popular vote
sorted_results = sorted(results, key=lambda x:x[2], reverse=True)

banner_length = 25
output = []
output.append("Election Results")
output.append('-' * banner_length)
output.append(f"Total Votes: {total_votes}")
output.append('-' * banner_length)
for result in sorted_results:
    output.append(f"{result[0]}: {result[1]:.3%} ({result[2]})")
output.append('-' * banner_length)
output.append(f"Winner: {sorted_results[0][0]}")
output.append('-' * banner_length)

output_filename = os.path.join('.', 'Resources', 'output.dat')
with open(output_filename, mode='wt', encoding='utf-8') as f:
    for line in output:
        f.write(line + '\n')
        print(line)