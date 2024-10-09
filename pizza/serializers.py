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
    
    def update(self, instance, validated_data):
        # Если передан id ресторана, обновляем связь
        if 'restaurant' in validated_data:
            restaurant_data = validated_data.pop('restaurant')
            restaurant = Restaurant.objects.get(id=restaurant_data['id'])  # Получаем ресторан по id
            instance.restaurant = restaurant

        # Обновляем остальные поля
        instance.pizza_name = validated_data.get('pizza_name', instance.pizza_name)
        instance.cheese_type = validated_data.get('cheese_type', instance.cheese_type)
        instance.dough_type = validated_data.get('dough_type', instance.dough_type)
        instance.secret_ingredient = validated_data.get('secret_ingredient', instance.secret_ingredient)

        # Сохраняем изменения
        instance.save()
        return instance