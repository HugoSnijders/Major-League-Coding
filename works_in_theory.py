#!/usr/bin/env python3
# Adapted from work by (c) 2016 David A. van Leeuwen
## that converts a "raw" tye of csv file from the PoW database into a json.

## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

#Now with (c) to Job Markink, Hugo Snijders, and Jamie March,
#This file takes all the wikipedia people data from a year range,
#and creates a csv file, Specifying BirthYear, DeathYear, If they are American or not,
#and if they are American, if they are a baseball player, football player, either, or neither. 
#Birth Year and Death Year are in years
#Not American = 0, American = 1
#American baseball player = 1 , American Football player = 2, Both = 3 , Neither = 0 

import json, logging, csv, re, sys, codecs
#From Here
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
#To here, is David's work
header = read_header("h.txt") #The headers should be read from the file h.txt 
out = [] #Create an empty output list
for year in range(1800, 2002): #These are birth years, no one who was born after 2002 is a professional athlete yet (cause age)
    file_path = 'years//' + str(year) #goes through the range of years 
    out += process_csv(file_path, header) 
with open('Life_Expectancy.csv', 'w', newline = '') as data: #write to a .csv file called Life Expectancy
    csvwriter = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC) #technical stuff
    csvwriter.writerow(['BirthYear', 'DeathYear', 'American', 'Athlete']) #we're writing birth year, death year, if they're American, and if they're an athlete (and what kind)
    for person in out: #For every person 
        persondata = [0] * 4 #Create a list in the loop (so for every person) thats just [0,0,0,0] 
        if 'birthYear' in person and 'deathYear' in person and person['birthYear'][0:4].isnumeric() and person['deathYear'][0:4].isnumeric(): # Only take into account people with a birth and death year,
		#life expectancy is useless when we don't have birth/death years cause missing values or they're still alive
        #To troubleshoot the problem that some people had a birth year in the format of '{digits' we're only counting if the birth/death year is numeric  
			persondata[0] = person['birthYear'][0:4]  #First 0 is amended to be the birth year, we only want the year so we ask for the first for digits 
            persondata[1] = person['deathYear'][0:4] #Second element is death year
            if 'description' in person and 'american' in str(person['description']).lower(): #Gotta make sure people have a description, or we have a key value error
			# then we check that American is in the description (cause we want Americans), we do the .lower function because we also want those labeled "American"
                persondata[2] = 1 #if you're American your 3rd value becomes 1, if not it stays 0 
                if 'team' in person: #Make sure we only get players, so like "football critic' is filtered out
                    if 'baseball' in person['description'].lower(): #again making sure we find "Baseball" and not just 'baseball' 
                        persondata[3] = 1 # 0 = none, 1 = baseball, 2 = football, 3 = both
                    if 'football' in person['description'].lower():
                        persondata[3] = 2
                        if 'baseball' in person['description'].lower():
                            persondata[3] = 3 #there aren't that many people who play both baseball and football in our data set, but just to be thorough, here is another group for them so one side isn't skewed. 
            csvwriter.writerow(persondata) #write all this stuff per person in the csv file
	