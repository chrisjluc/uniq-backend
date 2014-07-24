from bs4 import BeautifulSoup
import urllib2
import json
import jsontree
import urlparse

url = "http://ugradcalendar.uwaterloo.ca/page/ENG-mechatronics-Engineering"
te = "Technical Elective"
ce = "Complementary Studies Elective"
el = "Elective"

def ParseCourseFromCell(cell):
	if cell.a is not None and cell.a.get('href') is not None:
		url = cell.a.get('href')
		try:
			#/courses.aspx?Code=CS&amp;Number=240
			par = urlparse.parse_qs(urlparse.urlparse(url).query)
			return par['Code'][0].strip() + par['Number'][0].strip()
		except:
			#TPM is in url check first
			if "TPM" in url:
				return "TPM"
			#/courses/CS/247
			param = url.split("/")
			return param[-2] + param[-1]
	#Certain electives
	if cell.string is not None:
		if te in cell.string:
			return te
		if ce in cell.string:
			return ce
		if el in cell.string:
			return el
		return cell.string
	return ""

def ParseHoursFromCell(cell):
	if cell.string is not None:
		return cell.string.strip()
	if cell.div is not None and cell.div.string is not None:
		return cell.div.string.strip()
	return ""

def ScrapeCoursesFromURL(url):
	response = urllib2.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source,"lxml")
	soup = soup.find(class_="MainContent")

	data= []
	index = -1
	for table in soup.find_all('table'):
		header = []

		for th in table.thead.tr.find_all('th'):
			if th.string is not None:
				header.append(th.string)
			elif th.div is not None:
				header.append(th.div.string)

		if ("Class" in header or "Cls" in header) and "Tut" in header and "Lab" in header:
			for table_row in table.tbody.find_all('tr'):
				
				m_course = ''
				m_class = ''
				m_tut = ''
				m_lab = ''
				#has the term in the row
				cells = table_row.find_all('td')
				if len(cells) == len(header):
					index+=1
					data.append([]);

					m_course = ParseCourseFromCell(cells[1])
					m_class = ParseHoursFromCell(cells[2])
					m_tut = ParseHoursFromCell(cells[3])
					m_lab = ParseHoursFromCell(cells[4])
				else:
					m_course = ParseCourseFromCell(cells[0])
					try:
						m_class = ParseHoursFromCell(cells[1])
					except:
						m_class = ''
					try:
						m_tut = ParseHoursFromCell(cells[2])
					except:	
						m_tut = ''
					try:
						m_lab = ParseHoursFromCell(cells[3])
					except:	
						m_lab = ''
				#print m_course

				data[index].append({'course_code':m_course,'Class':m_class,'tut':m_tut,'lab':m_lab})
	return data
	
data = ScrapeCoursesFromURL(url)		
with open('program_courses.json', 'w') as program_courses:
	json.dump(data, program_courses, indent=4)

