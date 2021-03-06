#####################################
# write_type_cont_person

# Input: 	person_lookup.json
# 			instance_types_transitive_en.ttl

# Output:	filtered_type.txt

# Description:
# Build a list that contains all types assigned to a person based on DBpedia's dataset

# @author: mreif
#####################################

import json
import sys

def write_type_cont_person():
	try:
		f_json = open('data_extracted/person_lookup.json','r',encoding="utf8")
	except IOError:
		print('Need to create person_lookup.json first. (Execute write_personlist_by_type.py)')

	# Load person lookup created by write_personlist_by_type.py (Maps: *page of person* -> True, if it is a Person)
	person_lookup = json.load(f_json)
	print("Load complete: person_lookup.json")
	f_json.close()

	f_in = open('data_raw/instance_types_transitive_en.ttl','r', encoding="utf8")
	f_out = open('data_extracted/filtered_type.txt','w+', encoding="utf8")
	
	next(f_in) #First Line is comment with date
	for line in f_in:
		#Read all type assignments
		splits=line.split()
		subject=splits[0]
		if person_lookup.get(subject)==True:
			# If type belongs to person, keep it
			f_out.write(line)

	f_in.close()
	f_out.close()

	print('write_type_cont_person - DONE')

if __name__ == "__main__":
	if len(sys.argv)>1:
		raise IOError("Overspecified")
	write_type_cont_person()