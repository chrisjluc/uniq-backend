import urllib2, json

#https://api.uwaterloo.ca/v2/courses/MATH.json?key=1d9d39de6c47fc4dfaed591420849ba2
key = '1d9d39de6c47fc4dfaed591420849ba2'
subject_url = 'https://api.uwaterloo.ca/v2/codes/subjects.json?key='+key

subject_response = urllib2.urlopen(subject_url)
subject_data = json.loads(subject_response.read())
subjects =  [info['subject'] for info in subject_data['data']]

courses_info = []
for subject in subjects:
	course_url = 'https://api.uwaterloo.ca/v2/courses/'+subject+'.json?key='+key
	response = urllib2.urlopen(course_url)
	data = json.loads(response.read())
	[courses_info.append(course) for course in data['data']]
	print course_url

with open('subjects_uw_api.json', 'w') as subjects_info_file:
  json.dump(subject_data, subjects_info_file, indent=4, sort_keys=True)
with open('course_uw_api.json', 'w') as outfile:
  json.dump(courses_info, outfile, indent=4, sort_keys=True)

