persons = [{'birth': 1910, 'death': 1993, 'description': 'american baseball player and coach', 'team': 'a mediocre team'}, 
			{'birth': 1920, 'death': 1997, 'description': 'American football player'}, 
			{'birth': 1910, 'death': 1982, 'description': 'croatian tennis player', 'team': 'yet another team'}, 
			{'birth': 1910, 'death': 1982, 'description': 'tennis player'}, 
			{'birth': 1910, 'description': 'tennis player'},
			{'birth': 1910, 'death': 1982, 'description': 'American football and baseball', 'team': 'yet another team'},]

persondata = [] # will contain all relevant fields for a person, to be written to file
# e.g. [birthyear, deathyear, is_american, sports_category]

for person in persons:
	persondata = [0] * 4
	if 'birth' in person and 'death' in person: # Only take into account people with a birth and death year
		persondata[0] = person['birth']  #First element is birth year
		persondata[1] = person['death'] #Second element is death year
		if 'american' in person['description'].lower():
			persondata[2] = 1 
			if 'team' in person: #Make sure we only get players
				if 'baseball' in person['description'].lower():
					persondata[3] = 1 # 0 = none, 1 = baseball, 2 = football, 3 = both
				if 'football' in person['description'].lower():
					persondata[3] = 2
					if 'baseball' in person['description'].lower():
						persondata[3] = 3 
		
		print(persondata)
	
	