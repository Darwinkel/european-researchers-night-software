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
	cd ern && python manage.py runserver