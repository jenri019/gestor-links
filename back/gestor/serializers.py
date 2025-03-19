from rest_framework import serializers, validators
from django.core.validators import RegexValidator
from .models import Genero

class GeneroSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,  # Puede ser opcional
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',  # Solo números
                message="Este campo solo puede contener letras sin espacios."
            )
        ]
    )

    class Meta:
        model = Genero
        fields = ['id', 'name']

    def validate_name(self, value):
        return value