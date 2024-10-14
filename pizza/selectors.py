from .models import Pizza
from .serializers import PizzaSerializer

def get_all_pizzas():
    try:
        try:
            items = Pizza.objects.all()
        except Pizza.DoesNotExist:
            return 404, {'error': 'Pizza not found.'}
        serializer = PizzaSerializer(items, many=True)
        return 200, serializer.data  # Возвращаем статус и данные
    except Exception as e:
        return 500, str(e)  # Возвращаем ошибку, если что-то пошло не так