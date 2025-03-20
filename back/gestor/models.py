from django.db import models
from django.db.models.fields import CharField, TextField, URLField, IntegerField, BooleanField, AutoField

# Create your models here.
class Genero(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)

class Item(models.Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=100)
    tipo = CharField(max_length=6, default="")
    description = TextField(max_length = 300, blank=True)
    url = URLField()
    current_chapter = IntegerField()
    on_going = BooleanField(default=True)
    generos = models.TextField(default="")

class Types(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)