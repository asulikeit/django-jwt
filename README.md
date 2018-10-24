# django-jwt

## create virtual development environment
	$ mkdir ~/downloads
	$ cd ~/downloads
	$ pip download --no-cache --proxy http://proxy:1234 setuptools wheel pip$ cd -
	$ virtualenv --no-download -extra-search-dir ~/downloads venv
    
## how to activate on windows
	PS> Get-ExecutionPolicy
	Restricted
	PS> Set-ExecutionPolicy RemoteSigned
    
## activate for virtual environment
	$ cd Scripts
	$ activate
	(venv) _
	(venv) deactivate (to exit v.env)
	
## install requirement libraries
	(venv) pip install -r requirements.txt
	(venv) pip freeze (or pip list)

## create Database (ex. postgresql)
	$ psql -U postgres -a -f ./create_postgresql_db.sql
	password for postgres:
	create role testusr LOGIN NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
	CREATE ROLE
	create database "TestusrDb" with owner = testusr ENCODING = 'UTF8' CONNECTION LIMIT = -1;
	CREATE DATABASE
	alter role testusr with password 'password1!';
	ALTER ROLE

## create DB schema
    $ python manager.py makemigrations users
    $ python manager migrate
    
## create super user
	$ python manager.py createsuperuser
	Username: admin
	Email: admin@test.com
	Password:
	Password (again):
	This password is too common.
	Bypass password validation and create user anyway? (y/N): y
	Superuser created successfully.
	
## start server
	$ python manage.py runserver