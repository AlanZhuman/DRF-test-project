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
from .selectors import *
from .services import *
 
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
    status_code, response = create_pizza(request)
    if status_code == 200:
        return Response(response, status=status.HTTP_201_CREATED)
    elif status_code == 400:
        return Response({'error: ':response}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error: ':response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@swagger_auto_schema(method='post', request_body=PizzaSerializer)
@api_view(['POST'])
def add_items_delayed(request):
    status_code, response = create_pizza_delayed(request)
    if status_code == 200:
        return Response(response, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['GET'])
def view_items(request):
    status_code, response = get_all_pizzas()
    
    if status_code == 200:
        return Response(response)
    elif status_code == 404:
        return Response({'error': 'No pizzas found.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@swagger_auto_schema(method='post',request_body=PizzaSerializer)
@api_view(['POST'])
def update_items(request, pizza_slug):
    status_code, response = update_pizza(request, pizza_slug)
    if status_code == 200:
        return Response(response)
    elif status_code == 404:
        return Response({'error': 'None pizza found.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_items(request, pizza_slug):
    status_code, response = delete_pizza(pizza_slug)
    if status_code == 202:
        return Response(status=status.HTTP_202_ACCEPTED)
    elif status_code == 404:
        return Response({'error': response}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
