FROM python:3.12-slim-bookworm

WORKDIR /usr/src/app
RUN adduser ern

RUN mkdir /usr/src/app/db
RUN chown -R ern:ern /usr/src/app

COPY build-requirements.txt ./
RUN pip install --no-cache-dir -r build-requirements.txt

USER ern

RUN python -m nltk.downloader punkt punkt_tab

COPY ern ./ern
WORKDIR /usr/src/app/ern

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure", "--noreload"]
