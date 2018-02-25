# TMT
Twitter Monitoring Tool, get in real time content of your interest from Twitter to increase the efficiency of your response

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

### Input definition
- Add Twitter keys
- Set keywords:
  - Fill target list
  - Fill direct references list
  - Fill false direct references list

### Test mode
- Ramp up server
```
python manage.py runserver 8000
```
- Send request to server
```
curl --max-time 1 http://127.0.0.1:8000/get_tweets
```

### Production mode
- Set DEBUG flag to False
- Set up Postgres database
- Set up Apache server
