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
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Read': '/all',
        'Create': '/create',
        'Update': '/update/pk',
        'Delete': '/delete/pk'
    }
 
    return Response(api_urls)

@swagger_auto_schema(method='post',request_body=RestaurantSerializer)
@api_view(['POST'])
def add_items(request):
    item = RestaurantSerializer(data=request.data)
 
    # validating for already existing data
    if Restaurant.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
       
@api_view(['GET'])
def view_items(request):
    items = Restaurant.objects.all()

    if items:
        serializer = RestaurantSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@swagger_auto_schema(method='post',request_body=RestaurantSerializer)
@api_view(['POST'])
def update_items(request, pk):
    item = Restaurant.objects.get(pk=pk)
    data = RestaurantSerializer(instance=item, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Restaurant, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
