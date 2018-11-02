import sys
from pprint import pprint as pp
def read_file(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
       #read the header, and convert to a list of columns
        header = f.readline()[:-1] #ignore the \n at the end of the line
        columns = header.split(',')

        #converting each line into a row list
        rows = [line[:-1].split(',') for line in f.readlines()]
        
    return columns, rows

def output_results(filename, total_votes, results):
    banner_length = 25
    output = []
    output.append("Election Results")
    output.append('-' * banner_length)
    output.append(f"Total Votes: {total_votes}")
    output.append('-' * banner_length)
    for result in results:
        output.append(f"{result[0]}: {result[1]:.3%} ({result[2]})")
    output.append('-' * banner_length)
    output.append(f"Winner: {results[0][0]}")
    output.append('-' * banner_length)
    with open(filename, mode='wt', encoding='utf-8') as f:
        for line in output:
            f.write(line + '\n')
            print(line)


def main(input_filename, output_filename):
    columns, rows = read_file(input_filename)
    total_votes = len(rows)
    #use set to get distinct candidates
    candidates = (set(row[columns.index('Candidate')] for row in rows))
    results = []
    for candidate in candidates:
        result = []
        result.append(candidate)
        total_votes_per_candidate = len([row for row in rows if row[columns.index('Candidate')] == candidate])
        result.append(round(total_votes_per_candidate/total_votes, 5))
        result.append(total_votes_per_candidate)
        results.append(result)
    sorted_results = sorted(results, key=lambda x:x[2], reverse=True)
    output_results(output_filename, total_votes, sorted_results)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])