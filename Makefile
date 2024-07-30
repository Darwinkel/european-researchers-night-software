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
	python -m nltk.downloader punkt # Needed for basic sentence tokenization
	cd ern && python3 manage.py makemessages -l nl
	cd ern && django-admin compilemessages
	cd ern && python manage.py runserver 0.0.0.0:8000

deploy-run:
	rsync -avx --delete -e 'ssh -p 22322' --progress ./ jetbrains@penthouse.darwinkel.net:~/ern
	ssh -t jetbrains@penthouse.darwinkel.net -p 22322 "cd ~/ern && poetry run make run"