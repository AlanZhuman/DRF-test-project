from rest_framework import serializers
from .models import Pizza, Restaurant

class PizzaSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.restaurant_name')  # Корректируем путь
    pizza_id = serializers.IntegerField(source='id', read_only=True)
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Pizza
        fields = ('pizza_id', 'pizza_name', 'slug', 'cheese_type', 'dough_type', 'secret_ingredient', 'restaurant_name')
        read_only_fields = ('pizza_id', 'slug')

    def create(self, validated_data):
        # Извлечение данных о ресторане
        restaurant_data = validated_data.pop('restaurant', None)
        if restaurant_data is None:
            raise serializers.ValidationError("Restaurant data must be provided.")

        restaurant_name = restaurant_data.get('restaurant_name')  # Извлекаем название ресторана

        # Проверка существования ресторана
        restaurant = Restaurant.objects.filter(restaurant_name=restaurant_name).first()
        if not restaurant:
            raise serializers.ValidationError(f"Restaurant '{restaurant_name}' does not exist.")

        # Создание пиццы с правильным объектом ресторана
        pizza = Pizza.objects.create(restaurant=restaurant, **validated_data)
        return pizza

    
    def update(self, instance, validated_data):
        if 'restaurant_name' in validated_data:
            restaurant_data = validated_data.pop('restaurant_name')
            restaurant = Restaurant.objects.get(restaurant_name=restaurant_data['restaurant_name'])  # Получаем ресторан по имени
            instance.restaurant = restaurant

        # Обновляем остальные поля
        instance.pizza_name = validated_data.get('pizza_name', instance.pizza_name)
        instance.cheese_type = validated_data.get('cheese_type', instance.cheese_type)
        instance.dough_type = validated_data.get('dough_type', instance.dough_type)
        instance.secret_ingredient = validated_data.get('secret_ingredient', instance.secret_ingredient)

        # Сохраняем изменения
        instance.save()
        return instance