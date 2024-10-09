from django.db.models import fields
from rest_framework import serializers
from .models import Restaurant
from pizza.serializers import PizzaSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    pizzas = PizzaSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields=("id", "restaurant_name", "restaurant_address", "pizzas")