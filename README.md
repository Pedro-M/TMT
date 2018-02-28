# Twitter Monitoring Tool (TMT)
Twitter Monitoring Tool, get in real time content of your interest from Twitter to increase the efficiency of your 
response

## Installation

This tool uses Python 3.5.2 version

### Python VirtualEnv Setup
Python requisites:
```
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
```
In the repository directory run:
```
python3 -m venv tmtenv
source tmtenv/bin/activate
pip install -r requirements.txt
```

### Database migration
```
python manage.py makemigrations tweets
python manage.py migrate
```

### User creation
```
python manage.py createsuperuser
```

## Run

The program is going to find all tweets that are generated in real time in the Twitter stream that contain the words you 
provide as input.

### Input definition
- Add Twitter keys:
  - Go to https://apps.twitter.com/ and sign in with your Twitter account
  - Go to Keys and Access Tokens
  - Fill the template keys.py with the four available keys and place it inside tmt/tweets/keys
- Set keywords to search:
  - Fill the template targets.py following the hints that are given there and place it inside tmt/tweets/input

### Test mode
- Ramp up server
```
python manage.py runserver 8000
```
- Send request to server
```
curl --max-time 1 http://127.0.0.1:8000/get_tweets
```
- Depending on the popularity of the keywords in Twitter the tweets will start showing up in the stdout of the 
server and they will be available in the web application for further postprocessing  

### Production mode
- Set DEBUG flag to False in settings.py
- Set up Postgres database: Follow instructions on docs/set_up_postgres.md
- Set up Apache server: Follow instructions on docs/set_up_apache.md

