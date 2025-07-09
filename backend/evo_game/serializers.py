# your_app/serializers.py
from rest_framework import serializers
from .models import Population

class PopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = '__all__'
