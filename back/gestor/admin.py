from django.contrib import admin

# Register your models here.
from .models import Genero, Item, Type

admin.site.register(Genero)
admin.site.register(Item)
admin.site.register(Type)