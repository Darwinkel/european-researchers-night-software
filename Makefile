format:
	ruff format ern

check:
	ruff check ern

typing:
	mypy ern/*.py

quality:
	make format
	make check
	make typing

run:
	python -m nltk.downloader punkt # Needed for basic sentence tokenization
	cd ern && python3 manage.py makemessages -l nl
	cd ern && django-admin compilemessages
	cd ern && python manage.py runserver