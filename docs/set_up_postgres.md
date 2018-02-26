# Set up Postgres for Django

## Installation
```
sudo apt-get install python3-dev libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE tweets;
CREATE USER myuser WITH PASSWORD 'password';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE tweets TO myuser;
```

## Django setup
In settings.py, modify the DATABASES variable to:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tweets',
        'USER': '<myuser>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```