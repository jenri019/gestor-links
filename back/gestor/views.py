from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import logging

from django.shortcuts import render
from django.http import HttpResponse

from .models import Genero
from .serializers import GeneroSerializer

def hello(request):
    return HttpResponse('Hola Mundo! from Gestor')

@api_view(['GET'])
def get_genres(request):
    genres = Genero.objects.all().values()
    data = list(genres)
    return Response({'data': data, 'status': status.HTTP_200_OK})


@api_view(['POST'])
def add_genres(request):
    serializer = GeneroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"error": 0, "message": "Se ha crreado el genero", "status": status.HTTP_201_CREATED})
    else:
        return Response({ "error": 1, "message": "Error al crear el genero", "data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST})
    
""" @api_view(['PUT'])
def update_genres(request):
    serializer = GeneroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"error": 0, "message": "Se ha crreado el genero", "status": status.HTTP_201_CREATED})
    else:
        return Response({ "error": 1, "message": "Error al crear el genero", "status": status.HTTP_400_BAD_REQUEST}) """