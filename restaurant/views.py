from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer
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
        'Update': '/update/restaurant_name',
        'Delete': '/delete/restaurant_name'
    }
 
    return Response(api_urls)

@swagger_auto_schema(method='post', request_body=RestaurantSerializer)
@api_view(['POST'])
def add_items(request):
    status_code, response = create_restaurant(request)
    if status_code == 200:
        return Response(response, status=status.HTTP_201_CREATED)
    elif status_code == 400:
        return Response({'error: ':response}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error: ':response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['GET'])
def view_items(request):
    status_code, response = get_all_restaurants()
    
    if status_code == 200:
        return Response(response)
    elif status_code == 404:
        return Response({'error': 'No restaurants found.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@swagger_auto_schema(method='post',request_body=RestaurantSerializer)
@api_view(['POST'])
def update_items(request, restaurant_slug):
    status_code, response = update_restaurant(request, restaurant_slug)
    if status_code == 200:
        return Response(response)
    elif status_code == 404:
        return Response({'error': 'None restaurant found.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': response}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_items(request, restaurant_slug):
    status_code, response = delete_restaurant(restaurant_slug)
    if status_code == 202:
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif status_code == 404:
        return Response({'error': response}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
