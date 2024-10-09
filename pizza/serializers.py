from rest_framework import serializers
from .models import Pizza, Restaurant

class PizzaSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(source='restaurant.id')  # Изменено

    class Meta:
        model = Pizza
        fields = ("id", 'pizza_name', 'cheese_type', 'dough_type', 'secret_ingredient', 'restaurant_id')

    def create(self, validated_data):
        restaurant_data = validated_data.pop('restaurant')
        restaurant = Restaurant.objects.get(id=restaurant_data['id'])  # Получаем ресторан по id
        pizza = Pizza.objects.create(restaurant=restaurant, **validated_data)
        return pizza