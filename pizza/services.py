from .models import Pizza
from .serializers import PizzaSerializer
from .tasks import celery_create_pizza

def update_pizza(request, pizza_slug):
    try:
        item = Pizza.objects.get(slug=pizza_slug)
    except Pizza.DoesNotExist:
        return 404, {'error': 'Pizza not found.'}

    data = PizzaSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return 200, data.data
    elif data.is_valid() == False:
        return 400, {'error': 'Provided data is invalid'}
    return 500, {'Serializer error:': data.errors}
    
def create_pizza(request):
    serializer = PizzaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return 200, serializer.data
    elif serializer.is_valid() == False:
        return 400, {'error': 'Provided data is invalid'}
    return 500, {'Serializer error:': serializer.errors}

def create_pizza_delayed(request_data):
    try:
        celery_create_pizza.delay(request_data.data)
        return 200, {'msg':'Task in process'}
    except Exception as e:
        return 500, {'error': e}


def delete_pizza(pizza_slug):
    try:
        item = Pizza.objects.get(slug=pizza_slug)
    except Pizza.DoesNotExist:
        return 404, {'error': 'Pizza not found.'}
    item.delete()
    return 202
