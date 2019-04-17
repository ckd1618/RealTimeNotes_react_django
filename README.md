# RealTimeNotes_react_django
A real time note taking app using websockets that uses react on the frontend and django on the backend

Terminal commands used to create the app:

pipenv install django  
pipenv shell  
django-admin startproject notes_project .  
code .  
django-admin startapp notes  
//now open settings and add 'notes' to the installed apps array  
python manage.py runserver  
//create your models  
python manage.py makemigrations
python manage.py migrate


