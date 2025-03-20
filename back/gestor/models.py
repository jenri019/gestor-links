from django.db import models
from django.db.models.fields import CharField, TextField, URLField, IntegerField, BooleanField, AutoField

# Create your models here.
class Genero(models.Model):
    GENERO_ID = AutoField(primary_key=True)
    GENERO_NAME = CharField(max_length=20)

class Type(models.Model):
    TYPE_ID = AutoField(primary_key=True)
    TYPE_NAME = CharField(max_length=20)

class Item(models.Model):
    ITEM_ID = AutoField(primary_key=True)
    ITEM_TITLE = CharField(max_length=100)
    ITEM_TYPE = models.ForeignKey(Type, on_delete=models.CASCADE)
    ITEM_ECRIPTION = TextField(max_length = 300, blank=True)
    ITEM_URL = URLField()
    ITEM_CURRENT_CHAPTER = IntegerField()
    ITEM_ON_GOING = BooleanField(default=True)
    ITEM_GENRES = models.TextField(default="")