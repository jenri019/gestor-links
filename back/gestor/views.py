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
    # Obtener todos los ítems y convertir a diccionarios
    genres = Genero.objects.all().values()
    # Convertir el QuerySet a una lista
    data = list(genres)
    # Devolver la lista como respuesta JSON
    return Response({'genres': data, 'status': status.HTTP_200_OK})

@api_view(['POST'])
def add_genres(request):
    serializer = GeneroSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        return Response({"message": "Género creado", "status": status.HTTP_201_CREATED})
    else:
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)