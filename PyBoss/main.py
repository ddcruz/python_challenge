import os
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


csvpath = os.path.join('.', 'Resources', 'employee_data.csv')

with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #get the header
    header = next(csvreader)
    #read the rest of the file
    lines = [line for line in csvreader]

columns = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]

rows = []
for line in lines:
    row = []
    #Emp ID
    row.append(line[header.index('Emp ID')])
    names = line[header.index('Name')].split(" ")
    #First Name
    row.append(names[0])
    #Last Name
    row.append(names[1])
    #DOB MM/DD/YYYY
    row.append(datetime.strptime(line[header.index('DOB')], '%Y-%m-%d').strftime('%m/%d/%Y'))
    #SSN PII
    row.append('***-**' + line[header.index('SSN')][-5:])
    #State 2 letter  abbr
    row.append(us_state_abbrev[line[header.index('State')]])
    rows.append(row)

#output the new format
outputcsvpath = os.path.join('.', 'Resources', 'employee_data_new.csv')
#csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
with open(outputcsvpath, mode='w', newline='') as outputcsvfile:
    csvwriter = csv.writer(outputcsvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #output the column headers
    csvwriter.writerow(columns)
    for row in rows:
        csvwriter.writerow(row)
