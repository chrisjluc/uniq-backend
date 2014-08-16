import json
import jsontree

course_file = 'course_uw_api.json'
program_file = 'mechatronics.json'
output_file = 'mechatronics1.json'

course_data = None
program_data = None
with open(course_file) as data_file:
	course_data = json.load(data_file)
with open(program_file) as data_file:
	program_data = json.load(data_file)
terms = program_data['degreeRequirements']['curriculum']
for term in terms:
	for course in term:
		subject = course['subject']
		catalog_number = course['catalog_number']
		if not subject or not catalog_number:
			continue;
		for data in course_data:
			if data['subject'] == subject and data['catalog_number'] == catalog_number:
				course['academic_level'] = data['academic_level']
				course['description'] = data['description']
				course['title'] = data['title']
				course['units'] = data['units']
				break;

program_data['degreeRequirements']['curriculum'] = terms
with open(output_file, 'w') as file:
  json.dump(program_data, file, indent=4, sort_keys=True)