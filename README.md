# European Researcher's Night Software

This Django application was used for the European Researcher's Night 2024 to collect data.

# Development installation
Dependencies are handled with Poetry. See `make run` for the recommend way to run the project.
Dutch translations are handled with Django's built-in translation system.

# Production deployment

Make sure to change `SECRET_KEY` to a random string and `ALLOWED_HOST` to the domain name of the production server in `docker-compose.yml` before deploying to production.

```bash
docker compose run --rm django-ern python manage.py migrate
docker compose run --rm django-ern python manage.py createsuperuser --username admin --email admin@localhost
docker compose up -d
```

You should also set up a reverse proxy with HTTPS, such as Traefik, to serve the application.

The `sqlite3` database is stored in a Docker volume, which is mounted in the container. The `db.sqlite3` file is created automatically if it does not exist.

# Model deployment
This project assumes that `EN_OPENAI_HOST` and `NL_OPENAI_HOST` refer to OpenAI-compatible endpoints, such as [vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html).
It also assumes that there is a separate deployment for the Dutch and English models.

For the European Researcher's Night, the CIT provided an SSH tunnel with port forwarding to the GPU machine. Ask them for the details.
Basically, you can create a tunnel to the GPU server with the below command on the host machine, and then reach it from Docker containers through `host.docker.internal`:

```bash
ssh -N -L 8890:localhost:8890 -L 8891:localhost:8891 gpu-machine-tunnel
```

# Getting a CSV dump of the data
Using the `sqlite3` command line tool, you can dump the collected data to a CSV file with the following commands:

```bash
sqlite3 db/db.sqlite3
.headers on
.mode csv
.output db.csv
SELECT * FROM webapp_sample;
.quit
```