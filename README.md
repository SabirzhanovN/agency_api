# Project stacks
In this project used python programming language, database postgres and ubuntu os, so you have to install python and postgres.

## Database
It is best to use postgres tool to build database:

```
$ sudo su postgres
$ psql
$ create database name_for_db;
```
## Git 
Clone this repository

```
$ git clone https://github.com/SabirzhanovN/agency_api.git
```

## Building
* install and active virtualenv

```
$ cd agency_api
$ sudo apt install python3-venv
$ python3 -m venv venv # or 'virtualenv venv'
$ source venv/bin/activate
$ pip install -r requirements.txt
```

* then create tables for database and start the server

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```

