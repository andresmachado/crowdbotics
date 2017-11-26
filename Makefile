run:
	python manage.py runserver

migrate:
	python manage.py migrate

shell:
	python manage.py shell

migrations:
	python manage.py makemigrations

install:
	pip install -r requirements.txt

build: install migrations migrate run
