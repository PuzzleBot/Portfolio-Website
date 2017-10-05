TABLE_ID = 0001

all:
	python2 manage.py runserver

migrate: projectTables

projectTables:
	python2 manage.py makemigrations ProjectSection
	python2 manage.py migrate ProjectSection
	python2 manage.py sqlmigrate ProjectSection $(TABLE_ID)