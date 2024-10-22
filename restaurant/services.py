from .models import Restaurant
from .serializers import RestaurantSerializer
from django.shortcuts import get_object_or_404

def update_restaurant(request, restaurant_slug):
    try:
        item = Restaurant.objects.get(slug=restaurant_slug)
    except Restaurant.DoesNotExist:
        return 404, {'error': 'Restaurant not found.'}

    data = RestaurantSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return 200, data.data
    elif data.is_valid() == False:
        return 400, {'error': 'Provided data is invalid'}
    return 500, {'Serializer error:': data.errors}
    
def create_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return 200, serializer.data
    elif serializer.is_valid() == False:
        return 400, {'error': 'Provided data is invalid'}
    return 500, {'Serializer error:': serializer.errors}

def delete_restaurant(restaurant_slug):
    try:
        item = Restaurant.objects.get(slug=restaurant_slug)
    except Restaurant.DoesNotExist:
        return 404, {'error': 'Restaurant not found.'}
    item.delete()
    return 202, {'msg':'Deleted successful'}