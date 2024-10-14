from .models import Restaurant
from .serializers import RestaurantSerializer

def get_all_restaurants():
    try:
        try:
            items = Restaurant.objects.all()
        except Restaurant.DoesNotExist:
            return 404, {'error': 'Pizza not found.'}
        serializer = RestaurantSerializer(items, many=True)
        return 200, serializer.data  # Возвращаем статус и данные
    except Exception as e:
        return 500, str(e)  # Возвращаем ошибку, если что-то пошло не так