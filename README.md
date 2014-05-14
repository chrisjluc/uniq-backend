Uniq
=========================
Python 2.7.6

Django 1.6.2

Django REST framework 2.3




####v0.1
Basic functionality of schools and faculties. Development server should on http://127.0.0.1:8000/

- Schools
  - schools/:id	- Get information about specific school	faculties	get all faculties
  - schools/update/:timestamp	- Gets schools that have been updated since that time	(Doesn't check nested objects date modified)
  - schools/location - Create new school location object
  - schools/image - Create new school image object
  - schools/ranking - Create new school ranking object

- Faculties
  - schools/:id/faculties	- Get all the faculties of that school
  - faculties/:id	- Get faculty with associated id
  - faculties - Gets all faculties, and can post to create new faculty objects
  - faculties/update/:timestamp	- Gets updated faculty objects
  - faculties/image - Create new school image object
