from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Genero

class GeneroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)  # Campo 'id' de solo lectura

    name = serializers.CharField(
        required=True,  # Campo obligatorio
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',  # Solo letras sin espacios
                message="Este campo solo puede contener letras sin espacios."
            )
        ]
    )

    class Meta:
        model = Genero
        fields = ['id', 'name']

    def validate_name(self, value):
        # Convierte el nombre a minúsculas para evitar duplicados insensibles a mayúsculas/minúsculas
        value = value.lower()

        # Verifica si el nombre ya existe en la base de datos
        if Genero.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Este género ya existe.")
        return value