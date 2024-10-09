from django.db.models import fields
from rest_framework import serializers
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField()

    class Meta:
        model = Pizza
        fields = ("id", 'pizza_name', 'cheese_type', 'dough_type', 'secret_ingredient', 'restaurant')