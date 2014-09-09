#Uniq

Python 2.7.6, Django 1.6.2, Django REST framework 2.3.12, MongoDb 2.5.5, mongoengine 0.8.7, django-filter 0.7

=
####v0.2

#####API Endpoint
- Schools
  - schools/  - school list
  - schools/:slug - school detail
  - schools/:id - school detail

- Faculties
  - faculties/ - faculty list
  - schools/:slug/faculties - faculty list by school
  - schools/:id/faculties - faculty list by school
  - schools/:slug/faculties/:slug - faculty detail
  - faculties/:id - faculty detail

- Programs
  - programs/ - program list
  - schools/:slug/faculties/:slug/programs - program list by school and faculty
  - faculties/:id/programs - program list by faculty id
  - schools/:slug/faculties/:slug/programs/:slug - program detail
  - programs/:id - program detail

- Explore
  - explore/schools/ - school list
  - explore/faculties/ - faculty list
  - explore/faculties/:schoolId - faculty list by school id
  - explore/programs/ - program list
  - explore/programs/:facultyId - program list by faculty id
  
  - explore/program:programId - specific program

- Featured
  - featured/ - featured list
