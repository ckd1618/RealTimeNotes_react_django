from rest_framework import generics
from . import models
from . import serializers

# . means from the current folder


class NoteList(generics.ListCreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    # the serializer will transform our Note model into useful json data


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer
    # this allows us to retrieve update destroy

