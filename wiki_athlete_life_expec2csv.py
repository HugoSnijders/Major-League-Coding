#!/usr/bin/env python3
# Adapted from work by (c) 2016 David A. van Leeuwen
## that converts a "raw" tye of csv file from the PoW database into a json.
## Specifically,
## - we use a short label (first line in the general CSV header)
## - "NULL" entries are simply left out
## - numbers are interpreted as numbers, not strings

#Now with (c) to Job Markink, Hugo Snijders, and Jamie March,
#This file takes all the wikipedia people data from a year range,
#and creates a csv file, Specifying BirthYear, DeathYear, If they are from a specific country or not,
#and if they are from the country, if they are a player of two different team sports, both, or neither. 
#Birth Year and Death Year are in years, 4 digits
#Not belong to country = 0, belonging to country = 1
	#belonging to country and playing sport 1 = 1 , belonging to country and playing sport2 = 2, 
	#Belonging to country and playing both sports = 3 , Belonging to country but not a player of either sport = 0 
#If you want to run the code for different countries/sports change the user parameters

import json, logging, csv, re, sys, codecs

# user parameters (should be all lowercase):
sport1 = 'football'
sport2 = 'cricket'
country_name = 'england' 
country_adj = 'english' 

#Start of David's code
floatre = re.compile("^\d+\.\d+$")
intre = re.compile("^\d+$")

def read_header(file="h.txt"): #make sure you have the h.txt in the same folder, otherwise don't touch this
    header=[]
    for line in open(file):
        header.append(line.strip())
    logging.info("%d lines in header", len(header))
    return header

def process_csv(file, header): #don't touch this unless you know what you're doing
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
#End of David's code
header = read_header("h.txt") 
#The headers should be read from the file h.txt (put this file in the same folder as that file) 
out = [] #Create an empty output list
for year in range(1990, 2002): 
#These are birth years, no one who was born after 2002 is a professional athlete yet (cause age)
    file_path = "years\\" + str(year) #goes through the range of years 
    out += process_csv(file_path, header) 
with open(country_name + '.csv', 'w', newline = '') as data: #write to a .csv file called the name of your country 
    csvwriter = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC) #technical stuff
    csvwriter.writerow(['BirthYear', 'DeathYear', country_adj.title(), 'Athlete'])
	#we're writing birth year, death year, if they're from the specified country, and if they're an athlete (and what kind)
    for person in out: #For every person 
        persondata = [0] * 4 
		#Create a list in the loop (so for every person) thats just [0,0,0,0]
		#These numbers will be appended to values, or representatives of values  
        if 'birthYear' in person and 'deathYear' in person and person['birthYear'][0:4].isnumeric() and person['deathYear'][0:4].isnumeric():
		# Only take into account people with a birth and death year,
		#life expectancy is useless when we don't have birth/death years cause missing values or they're still alive
        #To troubleshoot the problem that some people had a birth year in the format of '{digits' we're only counting if the birth/death year is numeric  
            persondata[0] = person['birthYear'][0:4] 
			#First 0 is amended to be the birth year, we only want the year so we ask for the first four digits 
            persondata[1] = person['deathYear'][0:4] #Second element is death year
            if 'description' in person and country_adj in str(person['description']).lower():
			#Gotta make sure people have a description, or we have a key value error
			# then we check that country_adj (for example american) is in the description (cause we want for example: american footballers),
			#we do the .lower function because we also want capitalized entries
                if 'team' in person:
				#Make sure we only get players, so like "sport2 critic" is filtered out. Remove this line to get non team sport athletes at your own risk. 
                    if sport1 in person['description'].lower():
					#again making sure we find for example 'Baseball' and not just 'baseball' 
                        persondata[3] = 1 # 0 = none, 1 = sport1, 2 = sport2, 3 = both
                    if sport2 in person['description'].lower():
                        persondata[3] = 2 #if person plays sport2 append the 3rd index to the value two 
                        if 'sport1' in person['description'].lower():
                            persondata[3] = 3 
							#there aren't that many people who play both sport1 and sport2 in general,
							#but just to be thorough, here is another group for them so one side isn't skewed. 
            csvwriter.writerow(persondata) #write all this stuff per person in the csv file
	