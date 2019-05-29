# RealTimeNotes_react_django
THIS IS AN EARLY EFFORT, THE FINISHED PRODUCT IS AT THIS REPO: https://github.com/ckd1618/notes  
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
//------  
pipenv install channels channels-redis  
//add 'channels', to installed apps in settings.py  
//create routing.py under notes_project  
// in settings.py add: ASGI_APPLICATION = "notes_project.routing.application"  as well as CHANNEL_LAYERS =  
//install redis, cd Program Files/Redis and run: redis-cli.exe
//under notes create: consumers.py create the class NoteCustomer
// under notes create the file: routing.py
//update notes_project/routing.py by  importing notes/routing.py
pipenv install channels-redis redis
pip install Twisted==19.2.0
//https://developercommunity.visualstudio.com/content/problem/409173/error-microsoft-visual-c-140-is-required.html

