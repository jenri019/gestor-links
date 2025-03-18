from django.db import models
from django.db.models.fields import CharField, AutoField
    
class Genero(models.Model):
    GENERO_ID = AutoField(primary_key=True)
    GENERO_NOMBRE = CharField(max_length=20)