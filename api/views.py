from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializers import *


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()

    #serialize the notes
    serialize = NoteSerializer(notes, many=True)

    #get data from serializes notes
    return Response(serialize.data)
   

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)

    #serialize the notes
    serializer = NoteSerializer(note, many=False)

    #get data from serializes notes
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    
@api_view(['PUT'])
def updateNote(request, pk):
    note = Note.objects.get(id=pk)

    #serialize data received from frontend
    serializer = NoteSerializer(instance=note, data=request.data)


    if serializer.is_valid():
        serializer.save()

    #get data from serializes notes
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Item deleted')

