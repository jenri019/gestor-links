from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Genero

class GeneroSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message="Este campo solo puede contener letras sin espacios."
            )
        ]
    )

    class Meta:
        model = Genero
        fields = ['id', 'name']

    def validate_name(self, value):
        return value