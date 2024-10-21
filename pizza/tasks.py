from .serializers import PizzaSerializer
from .models import Pizza
from celery import shared_task
from pizza_restaurants.celery import app

@shared_task()
def celery_create_pizza(request_data):
    serializer = PizzaSerializer(data=request_data)

    if serializer.is_valid():
        serializer.save()

@app.task()
def delete_pizza_celery_schedule():
    oldest_object = Pizza.objects.order_by('updated_at').first()
    oldest_object.delete()