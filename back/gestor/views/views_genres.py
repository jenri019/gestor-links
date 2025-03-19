from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Genero
from ..serializers import GeneroSerializer

#
@api_view(['GET'])
def get_genres(request):
    try:
        genres = Genero.objects.all().values()
        data = list(genres)
        return Response({
            'data': data,
            'status': status.HTTP_200_OK
        })
    except Genero.DoesNotExist:
        return Response({
            "message": "Error al obtener los géneros",
            "status": status.HTTP_404_NOT_FOUND
        })


@api_view(['POST'])
def add_genres(request):
    serializer = GeneroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
    
            "message": "Se ha crreado el genero",
            "status": status.HTTP_201_CREATED
        })
    else:
        return Response({
            "message": "Error al crear el genero",
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })
    
@api_view(['PUT'])
def update_genres(request):
    id = request.data.get('id')
    if not id:
        return Response({
            "message": "El campo 'id' es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        })

    try:
        genero = Genero.objects.get(id=id)
    except Genero.DoesNotExist:
        return Response({
            "message": "El género no existe",
            "status": status.HTTP_404_NOT_FOUND
        })

    serializer = GeneroSerializer(genero, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Se ha actualizado el genero",
            "status": status.HTTP_201_CREATED
        })
    else:
        return Response({
            "message": "Error al actualizar el genero",
            "data": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })
    
@api_view(['DELETE'])
def delete_genres(request):
    id = request.data.get('id')
    if not id:
        return Response({
            "message": "El campo 'id' es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        })

    try:
        genero = Genero.objects.get(id=id)
    except Genero.DoesNotExist:
        return Response({
            "message": "El género no existe",
            "status": status.HTTP_404_NOT_FOUND
        })
    
    genero.delete()
    return Response({
        "message": "Se ha eliminado el genero",
        "status": status.HTTP_200_OK
    })