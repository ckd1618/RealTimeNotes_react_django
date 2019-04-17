# register our new path to the views we just created
from django.urls import path
from . import views  # imports NoteList and NoteDetail from views.py

urlpatterns = [
    path("", views.NoteList.as_view()),  # the default url will list everything
    path("<int:pk>/", views.NoteDetail.as_view()),
    # api/v1/notes/1 here the int from the path is the 1 in the url
]
