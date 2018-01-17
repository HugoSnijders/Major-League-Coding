#!/usr/bin/env python3
# (c) 2016 David A. van Leeuwen

## This file converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

import json, logging, csv, re, sys, codecs

floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="h.txt"):
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

def process_csv(file, header):
    out=[]
    stdin = file == "-"
    fd = sys.stdin if stdin else codecs.open(file, 'r', 'UTF-8')
    reader = csv.reader(fd)
    for nr, row in enumerate(reader):
        logging.debug("%d fields in line %d", len(row), nr)
        d = dict()
        out.append(d)
        for i, field in enumerate(row):
            if field != "NULL":
                if floatre.match(field):
                    d[header[i]] = float(field)
                elif intre.match(field):
                    d[header[i]] = int(field)
                else:
                    d[header[i]] = field
    if not stdin:
        fd.close()
    return out

header = read_header("h.txt")
out = []
out_filtered = []
for year in range(1800, 2002): #These are birth years, no one who was born after 2000 is a professional athlete yet (cause age)
    file_path = 'years//' + str(year) #go through the range of years 
    out += process_csv(file_path, header)
for line in out: #take this part out to get all the part out to get all the people not just athletes
    if 'team' in line:
        out_filtered.append(line) #if they're in a team add their information
#with open("years.json", "w") as s: #save as json
#    json.dump(out_filtered, s, indent=4, ensure_ascii=True)
#with open('years.json') as info:
#    filtered = json.load(info)
with open('test.csv', 'w', newline = '') as data: #write to csv, this is how you split the line
    csvwriter = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC) #technical stuff
    csvwriter.writerow(['BirthYear', 'DeathYear', 'Description']) #we're writing birth year, death year, description, these are the headers
    for line in out_filtered: #change this to variable out instead of out_filtered in case you are doing this for all people 
        if 'birthYear' in line and 'deathYear' in line and 'description' in line: #if all three of these variables are accounted for (not null)
             csvwriter.writerow([line['birthYear'][0:4], line['deathYear'][0:4], line['description']]) #use the index to write only the year, cause some of the birthYear has month, day, time, etc
        elif 'birthYear' in line and 'description' in line: # To get people who are still alive as well
             csvwriter.writerow([line['birthYear'][0:4], "2018", line['description']]) #we're writing 2018 if there is no death year, that means our nulls because of missing values, and people who are still alive are given the 'death year' of 2018
			 
"""for year in range(1800, 2001):
    file_path = 'years//' + str(year)
    out += process_csv(file_path, header)
for line in out:
    out_filtered.append(line)
with open('wikipeople.csv', 'w', newline='' ) as data:
    csvwriter = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['BirthYear', 'DeathYear'])
    for line in out_filtered:
        if 'birthYear' in line and 'deathYear' in line:
            csvwriter.writerow([line['birthYear'][0:4], line['deathYear'][0:4]])""" # ALL THE PEOPLE
