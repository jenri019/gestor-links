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
        # Obtener todos los items con sus relaciones optimizadas
        items = Item.objects.all().select_related('ITEM_TYPE').values(
            'ITEM_ID',
            'ITEM_TITLE',
            'ITEM_TYPE__TYPE_NAME',  # Acceder al nombre del tipo relacionado
            'ITEM_DESCRIPTION',
            'ITEM_URL',
            'ITEM_CURRENT_CHAPTER',
            'ITEM_ON_GOING',
            'ITEM_GENRES'
        )
        
        # Renombrar las columnas
        renamed_items = [
            {
                'id': item['ITEM_ID'],
                'title': item['ITEM_TITLE'],
                'type': item['ITEM_TYPE__TYPE_NAME'],
                'description': item['ITEM_DESCRIPTION'],
                'url': item['ITEM_URL'],
                'current_chapter': item['ITEM_CURRENT_CHAPTER'],
                'on_going': item['ITEM_ON_GOING'],
                'genres': item['ITEM_GENRES']
            }
            for item in items
        ]
        
        return Response({
            'data': renamed_items,
            "message": "Items obtenidos correctamente",
            'status': status.HTTP_200_OK
        })
    except Exception as e:
        # Capturar cualquier error inesperado y devolver una respuesta informativa
        return Response({
            "message": "Error al obtener los items",
            "error": str(e),  # Incluir el mensaje de error para debugging
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
    

@api_view(['PUT'])
def update_items(request):
    id = request.data.get('id')
    generos = request.data.get('generos', [])
    req_type = request.data.get('type')
    title = request.data.get('title')
    description = request.data.get('description')
    url = request.data.get('url')
    current_chapter = request.data.get('current_chapter', 0)

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
    
    # Convertir el array de generos en un string JSON
    generos_str = json.dumps(generos)

    if Item.objects.filter(ITEM_TITLE=title).exclude(ITEM_ID=id).exists():
        return Response({
            "message": "Este titulo ya se encuentra registrado",
            "status": status.HTTP_400_BAD_REQUEST
        })

    # Actualizar el nombre del género
    item.ITEM_TITLE = title
    item.ITEM_TYPE=type_instance  # Usar la instancia de Type
    item.ITEM_DESCRIPTION = description
    item.ITEM_URL = url
    item.ITEM_CURRENT_CHAPTER = current_chapter
    item.ITEM_GENRES = generos_str

    item.save()

    return Response({
        "message": "Se ha actualizado el registro",
        "status": status.HTTP_201_CREATED
    })


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