from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Type

#OBTIEEN EL LISTADO DE types
@api_view(['GET'])
def get_types(request):
    try:
        types = Type.objects.all().values()
        data = list(types)
        return Response({
            'data': data,
            "message": "Tipos obtenidos",
            'status': status.HTTP_200_OK
        })
    except Type.DoesNotExist:
        return Response({
            "message": "Error al obtener los tipos",
            "status": status.HTTP_404_NOT_FOUND
        })
    
@api_view(['POST'])
def add_types(request):
    name = request.data.get('name')

    if not name:
        return Response({
            "message": "El campo 'name' es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        })

    if Type.objects.filter(TYPE_NAME=name).exists():
        return Response({
            "message": "El tipo ya existe",
            "status": status.HTTP_400_BAD_REQUEST
        })
    
    try:
        Type.objects.create(
            TYPE_NAME=name
        )
        return Response({
            "message": "Se ha creado el tipo",
            "status": status.HTTP_201_CREATED
        })
    except Type.DoesNotExist:
        return Response({
            "message": "Error al crear los tipos",
            "status": status.HTTP_404_NOT_FOUND
        })