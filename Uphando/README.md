# Uphando

In the apps directory go into the apps.py for each folder 
(core, job, notification, userprofile) and add "apps." to the name. 
So for the core folder for example, in apps.py you should have
	name = 'apps.core'  

(run if pipenv is not available) pip install pipenv
set PIPENV_VENV_IN_PROJECT="enabled"
pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
 
Server address: 127.0.0.1:8000 

Click the link and the app will launch.

