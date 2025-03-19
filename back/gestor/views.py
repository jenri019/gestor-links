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
    return Response({
        'data': data,
        'status': status.HTTP_200_OK
    })


@api_view(['POST'])
def add_genres(request):
    serializer = GeneroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "error": 0,
            "message": "Se ha crreado el genero",
            "status": status.HTTP_201_CREATED
        })
    else:
        return Response({
            "error": 1,
            "message": "Error al crear el genero",
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })
    
@api_view(['PUT'])
def update_genres(request):
    id = request.data.get('id')
    if not id:
        return Response({
            "error": 1,
            "message": "El campo 'id' es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        })

    try:
        genero = Genero.objects.get(id=id)
    except Genero.DoesNotExist:
        return Response({
            "error": 1,
            "message": "El género no existe",
            "status": status.HTTP_404_NOT_FOUND
        })

    serializer = GeneroSerializer(genero, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "error": 0,
            "message": "Se ha actualizado el genero",
            "status": status.HTTP_201_CREATED
        })
    else:
        return Response({
            "error": 1,
            "message": "Error al actualizar el genero",
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })