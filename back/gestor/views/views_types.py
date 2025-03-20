from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Types

#OBTIEEN EL LISTADO DE types
@api_view(['GET'])
def get_types():
    try:
        types = Types.objects.all().values()
        data = list(types)
        return Response({
            'data': data,
            'status': status.HTTP_200_OK
        })
    except Types.DoesNotExist:
        return Response({
            "message": "Error al obtener los tipos",
            "status": status.HTTP_404_NOT_FOUND
        })