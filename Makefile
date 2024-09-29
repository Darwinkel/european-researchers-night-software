format:
	ruff format ern

check:
	ruff check ern

typing:
	mypy .

quality:
	make format
	make check
	make typing

run:
	python -m nltk.downloader punkt punkt_tab # Needed for basic sentence tokenization
	cd ern && python3 manage.py makemessages -l nl
	cd ern && django-admin compilemessages
	cd ern && python manage.py runserver 0.0.0.0:8000

docker-build:
	poetry export -f requirements.txt --output build-requirements.txt
	docker compose build
	rm build-requirements.txt

docker-migrate:
	docker compose run --rm django-ern python manage.py migrate
	docker compose run --rm django-ern python manage.py createsuperuser --username admin --email admin@localhost

docker-run:
	docker compose up -d && docker compose logs -f

docker-deploy:
	docker save european-researchers-night-software-django-ern | ssh -C hostname docker load
