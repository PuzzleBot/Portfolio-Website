TABLE_ID = 0001
PYTHON = python2

all:
	$(PYTHON) manage.py runserver

migrate: projectTables

projectTables:
	$(PYTHON) manage.py makemigrations ProjectSection
	$(PYTHON) manage.py migrate ProjectSection
	$(PYTHON) manage.py sqlmigrate ProjectSection $(TABLE_ID)