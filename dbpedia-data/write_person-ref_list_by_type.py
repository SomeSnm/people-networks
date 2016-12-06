import json
import sys

def write_person_ref_list_by_type():

	f_in = open('data_raw/instance_types_transitive_en.ttl','r', encoding="utf8")
	f_out = open('data_extracted/person_&_ref_list_manual.txt','w+', encoding="utf8")

	# Filter:	- fictional characters (note: some are still in: Something like Miss Marple isnt tagged accordingly)
	# 			- the awkward entires ending "__1" (often duplicates of football players, famous people)

	unwanted=dict() # Filter dict
	person=dict() # Store all persons (unfiltered)
	final_dict=dict() # Dict for all persons that pass the filter (matches content of f_out)
	previous_subject=None

	for line in f_in:
		splits=line.split()
		subject=splits[0]
		value=splits[2]
		if previous_subject==None:
			previous_subject=subject

		if value == '<http://dbpedia.org/ontology/FictionalCharacter>':
			unwanted[subject]=True

		if (value == '<http://dbpedia.org/ontology/Person>' or value == '<http://schema.org/Person>' or value == '<http://xmlns.com/foaf/0.1/Person>'):
			person[subject]=True

		if previous_subject!=subject and unwanted.get(previous_subject)==None and person.get(previous_subject)==True :
			f_out.write(previous_subject+"\n")
			final_dict[previous_subject]=True
			previous_subject=subject
		else:
			previous_subject=subject

	f_in.close()
	f_out.close()

	with open('data_extracted/person_ref_lookup.json','w+', encoding='utf8') as f_json:
		json.dump(final_dict, f_json, ensure_ascii=False)

	print('DONE!')

if __name__ == "__main__":
	if len(sys.argv)>1:
		raise IOError("Overspecified")
	write_person_ref_list_by_type()