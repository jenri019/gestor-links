from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Item

#
@api_view(['GET'])
def get_items(request):
    try:
        items = Item.objects.all().values()
        data = list(items)
        return Response({
            'data': data,
            'status': status.HTTP_200_OK
        })
    except Item.DoesNotExist:
        return Response({
            "message": "Error al obtener los géneros",
            "status": status.HTTP_404_NOT_FOUND
        })