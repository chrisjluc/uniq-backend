from bs4 import BeautifulSoup
import urllib2
import re

aboutURL = "https://uwaterloo.ca/about/who-we-are"
contactURL = "https://uwaterloo.ca/find-out-more/contact-us"
wikiURL = "http://en.wikipedia.org/wiki/"
name = "University of Waterloo"

def getAbout():
	response = urllib2.urlopen(aboutURL)
	page_source = response.read()
	soup = BeautifulSoup(page_source,"lxml")
	mainText =  soup.find(class_="field-item even")
	data = {'about': ''}
	for child in mainText.contents:
		tag_name = child.name
		if tag_name == None or child.string == None:
			continue
		if tag_name == 'p':
			data['about'] = str(data['about']) + ' ' + child.string.encode('ascii','ignore')
		if tag_name == 'h3':
			break

	return data['about']

def getContactInfo():
	response = urllib2.urlopen(contactURL)
	page_source = response.read()
	soup = BeautifulSoup(page_source,"lxml")
	data = {}
	data['email'] = soup.find('a', text = re.compile('\w@uwaterloo.ca')).text
	data['phoneNumber'] = soup.find('strong', text = re.compile('\d{3}-\d{3}-\d{4}')).text.split(" ")[0]
	return data

print getContactInfo()