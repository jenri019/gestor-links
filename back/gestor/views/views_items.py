from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Item, Genero

#OBTIEEN EL LISTADO DE ITEMS
@api_view(['GET'])
def get_items():
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
    
@api_view(['POST'])
def add_items(request):
    generos_ids = request.data.get('generos', [])

    # Verificar que vengan los generos en el request
    if not generos_ids:
        return Response({
            "message": "El genero es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Verificar si todos los IDs existen en la tabla de generos
    generos_existentes = Genero.objects.filter(id__in=generos_ids)
    if generos_existentes.count() != len(generos_ids):
        return Response({
            "message": "Se encontraron generos inexistentes",
            "status": status.HTTP_404_NOT_FOUND
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Convertir generos_existentes en un array de strings con los nombres de los generos
    generos_nombres = generos_existentes.values_list('name', flat=True)
    # Convertir el array en una caena separada por comas
    generos_str = ', '.join(generos_nombres)

    #Se intenta crear el item
    try:
        Item.objects.create(
            title = request.data.get('title'),
            description = request.data.get('description'),
            tipo = request.data.get('type'),
            url = request.data.get('url'),
            current_chapter = request.data.get('current_chapter'),
            generos = generos_str
        )

        return Response({
            "message": "Item creado exitosamente",
            "status": status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({
            "message": "Error al crear el item:",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)