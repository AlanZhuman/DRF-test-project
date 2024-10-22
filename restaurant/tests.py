import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Restaurant

@pytest.mark.django_db
def test_create_restaurant():
    client = APIClient()

    test_data = {
        "restaurant_name": 'test_restaurant_name',
        "restaurant_address": 'test_restaurant_address'
    }

    response =  client.post(reverse('add-restaurant'), data=test_data, format='json')

    assert response.status_code == 201

@pytest.mark.django_db
def test_view_restaurants():
    client = APIClient()

    test_data = {
        "restaurant_name": 'test_restaurant_name',
        "restaurant_address": 'test_restaurant_address'
    }

    response =  client.post(reverse('add-restaurant'), data=test_data, format='json')
    assert response.status_code == 201

    test_data = {
        "restaurant_name": 'test_restaurant_name_2',
        "restaurant_address": 'test_restaurant_address_2'
    }

    response =  client.post(reverse('add-restaurant'), data=test_data, format='json')
    assert response.status_code == 201

    response = client.get(reverse('view-restaurants'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_update_restaurants():
    client = APIClient()

    test_data = {
        "restaurant_name": 'test_restaurant_name',
        "restaurant_address": 'test_restaurant_address'
    }

    response =  client.post(reverse('add-restaurant'), data=test_data, format='json')
    assert response.status_code == 201

    test_data = {
        "restaurant_name": 'updated_restaurant_name',
        "restaurant_address": 'updated_restaurant_address'
    }

    restaurant = Restaurant.objects.get(restaurant_name="test_restaurant_name")
    restaurant_slug = restaurant.slug  # Используем сгенерированный slug
    assert Restaurant.objects.filter(slug=restaurant_slug).exists()

    response =  client.post(reverse('update-restaurant', args=[restaurant_slug]), data=test_data, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_restaurants():
    client = APIClient()

    test_data = {
        "restaurant_name": 'test_restaurant_name',
        "restaurant_address": 'test_restaurant_address'
    }

    response =  client.post(reverse('add-restaurant'), data=test_data, format='json')
    assert response.status_code == 201

    restaurant = Restaurant.objects.get(restaurant_name="test_restaurant_name")
    restaurant_slug = restaurant.slug  # Используем сгенерированный slug
    assert Restaurant.objects.filter(slug=restaurant_slug).exists()

    response =  client.delete(reverse('delete-restaurant', args=[restaurant_slug]), format='json')
    assert response.status_code == 204