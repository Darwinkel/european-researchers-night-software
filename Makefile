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
	cd ern && python manage.py runserver