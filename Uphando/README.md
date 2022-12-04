# Uphando

In the apps directory go into the apps.py for each folder 
(core, job, userprofile) and add "apps." to the name. 
So for the core folder for example, in apps.py you should have
	name = 'apps.core'  

To run Uphando, cd into the Uphando folder containing the manage.py file and follow whichever of the options best suits you.

# Option 1:
If makefile functionality is available, run the command:
	make run

# Option 2:
If makefile functionality is not available, run the following commands:
(run if pipenv is not available) pip install pipenv
set PIPENV_VENV_IN_PROJECT="enabled"
pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
 
Server address: 127.0.0.1:8000 

Click the link and the app will launch.

