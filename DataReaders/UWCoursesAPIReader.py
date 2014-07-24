import urllib2, json

#https://api.uwaterloo.ca/v2/courses/MATH.json?key=1d9d39de6c47fc4dfaed591420849ba2
key = '1d9d39de6c47fc4dfaed591420849ba2'
subject_url = 'https://api.uwaterloo.ca/v2/codes/subjects.json?key='+key

def getSubjectData():
	subject_response = urllib2.urlopen(subject_url)
	return json.loads(subject_response.read())

def getCourseData(subject_data):
	subjects =  [info['subject'] for info in subject_data['data']]
	courses_info = []
	for subject in subjects:
		course_url = 'https://api.uwaterloo.ca/v2/courses/'+subject+'.json?key='+key
		response = urllib2.urlopen(course_url)
		data = json.loads(response.read())
		[courses_info.append(course) for course in data['data']]
		print course_url
	return courses_info

subject_data = getSubjectData()
with open('subjects_uw_api.json', 'w') as subjects_info_file:
  json.dump(subject_data['data'], subjects_info_file, indent=4, sort_keys=True)
  
course_data = getCourseData(subject_data)	
with open('course_uw_api.json', 'w') as outfile:
  json.dump(course_data, outfile, indent=4, sort_keys=True)

