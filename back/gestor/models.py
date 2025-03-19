from django.db import models
from django.db.models.fields import CharField, AutoField

# Create your models here.
class Genero(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)