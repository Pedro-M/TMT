# Set up Apache server

## Installation
```
sudo apt-get install apache2 libapache2-mod-wsgi-py3
```
- In /etc/apache2, select the port the server is listen in in ports.conf
- Place the tmt.conf in sites-available folder and activate it with:
```
sudo a2ensite sites-available/tmt.conf
sudo service apache2 restart
```

## Django setup
```
python manage.py collectstatic
```
In settings.py, add your server IP to the ALLOWED_HOSTS variable
