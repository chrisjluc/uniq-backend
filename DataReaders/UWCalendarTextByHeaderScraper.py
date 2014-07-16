from bs4 import BeautifulSoup
import urllib2
import json
import jsontree

url_string = "http://ugradcalendar.uwaterloo.ca/page/ENG-Mechatronics-Engineering"

def ParseTextFromURL(url):
	response = urllib2.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source,"lxml")
	soup = soup.find(class_="MainContent")

	data = []
	keys = []

	for child in soup.children:
		tag_name = child.name
		if tag_name == None or child.string == None:
			continue
		#When the json tree is empty, the first elements are description for the program
		#TODO: Handle unicode better
		elif len(data) == 0:
			desc = "description"
			data.append(child.string.encode('ascii','ignore'))
			keys.append(desc)
		#Get last key and append the current child to that
		elif tag_name == 'p':
			key = keys[-1]
			data[-1] = str(data[-1]) + ' ' + child.string.encode('ascii','ignore')
		elif tag_name == 'h3' or tag_name == 'h4':
			keys.append(child.string)
			data.append('')
			#if child previous is header thats the key

	json_data = {}
	if len(keys) == len(data):
		for i in xrange(0,len(keys)):
			if len(data[i]) is not 0:
				json_data[keys[i]] = data[i].strip()

	return json_data
	
data = ParseTextFromURL(url_string)
with open('uw_calendar_textbyheader.json', 'w') as filename:
  json.dump(data, filename, indent=4)

'''
for link in soup.find_all('a'):
    print(link.get('href'))
'''