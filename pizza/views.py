from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pizza, Restaurant
from .serializers import PizzaSerializer
from rest_framework import serializers
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Read': '/all',
        'Create': '/create',
        'Update': '/update/pk',
        'Delete': '/delete/pk'
    }
 
    return Response(api_urls)

@swagger_auto_schema(method='post', request_body=PizzaSerializer)
@api_view(['POST'])
def add_items(request):
    # Создание сериализатора с входными данными
    serializer = PizzaSerializer(data=request.data)
    
    # Проверка на существование пиццы
    if serializer.is_valid():
        # Проверка, существует ли ресторан
        restaurant_id = serializer.validated_data.get('restaurant', {}).get('id')
        if not Restaurant.objects.filter(id=restaurant_id).exists():
            return Response({'error': 'Restaurant not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Сохранение новой пиццы
        serializer.save()  # Теперь это сохранит пиццу с правильной ссылкой на ресторан
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки валидации
    
@api_view(['GET'])
def view_items(request):
    items = Pizza.objects.all()

    if items:
        serializer = PizzaSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@swagger_auto_schema(method='post',request_body=PizzaSerializer)
@api_view(['POST'])
def update_items(request, pk):
    item = Pizza.objects.get(pk=pk)
    data = PizzaSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Pizza, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
