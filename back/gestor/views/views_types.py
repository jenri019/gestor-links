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
    try:
        Type.objects.create(
            name=request.data.get('name')
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