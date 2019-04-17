# RealTimeNotes_react_django
A real time note taking app using websockets that uses react on the frontend and django on the backend

Terminal commands used to create the app:

pipenv install django  
pipenv shell  
django-admin startproject notes_project .  
code .  
django-admin startapp notes  
//now open settings.py and add 'notes' to the installed apps array  
python manage.py runserver  
//create your models  
python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver
//localhost:8000/admin is available, but you will have to set up the password
python manage.py createsuperuser --username=admin
//ckd1618@gmail.com
//password123
//under admin.py import and register the Note model
pipenv install djangorestframework
pipenv install django-cors-headers
//now add both of these to settings.py array
//also add CorsMiddleware to the middleware array
//create a file under notes folder called serializers.py and create the class NoteSerializer
//in notes/views.py create the NoteList and NoteDetail classes
// under notes folder create the file urls.py
//under notes_project folder import include, and update this page
//add CORS_ORIGIN_WHITELIST = (localhost:3000,) to notes_project/settings.py
