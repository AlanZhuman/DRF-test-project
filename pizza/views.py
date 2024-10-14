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
        'Update': '/update/pizza_name',
        'Delete': '/delete/pizza_name'
    }
 
    return Response(api_urls)

@swagger_auto_schema(method='post', request_body=PizzaSerializer)
@api_view(['POST'])
def add_items(request):
    serializer = PizzaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
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
def update_items(request, pizza_slug):
    item = Pizza.objects.get(slug=pizza_slug)
    data = PizzaSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pizza_slug):
    item = get_object_or_404(Pizza, slug=pizza_slug)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
