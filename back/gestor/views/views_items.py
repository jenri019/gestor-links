import json
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Item, Genero, Type

#OBTIEEN EL LISTADO DE ITEMS
@api_view(['GET'])
def get_items(request):
    try:
        items = Item.objects.all().values()
        data = list(items)
        return Response({
            'data': data,
            "message": "Items obtenidos",
            'status': status.HTTP_200_OK
        })
    except Item.DoesNotExist:
        return Response({
            "message": "Error al obtener los géneros",
            "status": status.HTTP_404_NOT_FOUND
        })


@api_view(['POST'])
def add_items(request):
    generos = request.data.get('generos', [])
    req_type = request.data.get('type')
    title = request.data.get('title')
    description = request.data.get('description')
    url = request.data.get('url')
    current_chapter = request.data.get('current_chapter', 0)

    # Verificar que vengan los generos en el request
    if not generos:
        return Response({
            "message": "El genero es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not req_type:
        return Response({
            "message": "El tipo es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        type_instance = get_object_or_404(Type, pk=req_type)
    except Exception as e:
        return Response({
            "message": "Tipo no encontrado",
            "error": str(e),
            "status": status.HTTP_404_NOT_FOUND
        }, status=status.HTTP_404_NOT_FOUND)

    # Verificar si todos los IDs existen en la tabla de generos
    generos_existentes = Genero.objects.filter(GENERO_ID__in=generos)
    if generos_existentes.count() != len(generos):
        return Response({
            "message": "Se encontraron generos inexistentes",
            "status": status.HTTP_404_NOT_FOUND
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Convertir generos_existentes en un array de strings con los nombres de los generos
    # generos_nombres = generos_existentes.values_list('name', flat=True)
    # Convertir el array en una caena separada por comas
    # generos_str = ', '.join(generos_nombres)

    # Convertir el array de generos en un string JSON
    generos_str = json.dumps(generos)

    #Se intenta crear el item
    try:
        Item.objects.create(
            ITEM_TITLE = title,
            ITEM_TYPE=type_instance,  # Usar la instancia de Type
            ITEM_DESCRIPTION = description,
            ITEM_URL = url,
            ITEM_CURRENT_CHAPTER = current_chapter,
            ITEM_GENRES = generos_str
        )

        return Response({
            "message": "Item creado exitosamente",
            "status": status.HTTP_201_CREATED
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({
            "message": "Error al crear el item:",
            "error": str(e),
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_items(request):
    id = request.data.get('id')
    if not id:
        return Response({
            "message": "El campo 'id' es requerido",
            "status": status.HTTP_400_BAD_REQUEST
        })

    try:
        item = Item.objects.get(ITEM_ID=id)
    except Item.DoesNotExist:
        return Response({
            "message": "El item no existe",
            "status": status.HTTP_404_NOT_FOUND
        })
    
    item.delete()
    return Response({
        "message": "Se ha eliminado el item",
        "status": status.HTTP_200_OK
    })