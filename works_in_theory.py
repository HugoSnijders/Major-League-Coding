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
def onlyLetters(inputString): #check if a string only contains letters 
    return not any(char.isdigit() for char in inputString)
onlyLetters('a23') == True
header = read_header("h.txt")
out = []
for year in range(1800, 2002): #These are birth years, no one who was born after 2000 is a professional athlete yet (cause age)
    file_path = 'years//' + str(year) #go through the range of years 
    out += process_csv(file_path, header)
with open('Life_Expectancy.csv', 'w', newline = '') as data: #write to csv, this is how you split the line
    csvwriter = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC) #technical stuff
    csvwriter.writerow(['BirthYear', 'DeathYear', 'American', 'Athlete']) #we're writing birth year, death year, description, these are the headers
    for person in out:
        persondata = [0] * 4
        #if 'birthYear' in person: print("Birthyear is: " + person['birthYear'] + ", Is numeric? : " + str(person['birthYear'][0:4].isnumeric()))
        if 'birthYear' in person and 'deathYear' in person and person['birthYear'][0:4].isnumeric() and person['deathYear'][0:4].isnumeric(): # Only take into account people with a birth and death year
            persondata[0] = person['birthYear'][0:4]  #First element is birth year
            persondata[1] = person['deathYear'][0:4] #Second element is death year
            if 'description' in person and 'american' in str(person['description']).lower():
                persondata[2] = 1 
                if 'team' in person: #Make sure we only get players
                    if 'baseball' in person['description'].lower():
                        persondata[3] = 1 # 0 = none, 1 = baseball, 2 = football, 3 = both
                    if 'football' in person['description'].lower():
                        persondata[3] = 2
                        if 'baseball' in person['description'].lower():
                            persondata[3] = 3 
            csvwriter.writerow(persondata)
	
	