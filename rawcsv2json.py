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
for year in range(1800, 2016):
    file_path = 'years//' + str(year)
    out += process_csv(file_path, header)
for line in out:
    if 'team' in line:
        out_filtered.append(line)
#with open("years.json", "w") as s:
#    json.dump(out_filtered, s, indent=4, ensure_ascii=True)
#with open('years.json') as info:
#    filtered = json.load(info)
with open('test.csv', 'w', newline = '') as data:
    csvwriter = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['BirthYear', 'DeathYear', 'Description'])
    for line in out_filtered:
        if 'birthYear' in line and 'deathYear' in line and 'description' in line:
             csvwriter.writerow([line['birthYear'][0:4], line['deathYear'][0:4], line['description']])
        elif 'birthYear' in line and 'description' in line:
             csvwriter.writerow([line['birthYear'][0:4], "NA", line['description']])
