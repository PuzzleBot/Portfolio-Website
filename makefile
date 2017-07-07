TABLE_ID = 0001

all:
	python manage.py runserver

migrate: projectTables

projectTables:
	python manage.py makemigrations ProjectSection
	python manage.py migrate ProjectSection
	python manage.py sqlmigrate ProjectSection $(TABLE_ID)