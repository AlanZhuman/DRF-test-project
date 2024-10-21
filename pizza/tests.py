import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Restaurant

@pytest.mark.django_db
def test_create_pizza():
    # Создаем ресторан
    restaurant = Restaurant.objects.create(restaurant_name="Test Restaurant", slug='test-restaurant', restaurant_address='Test Address')

    client = APIClient()
    test_data = {
        "pizza_name": "string",
        "cheese_type": "string",
        "dough_type": "THIN",
        "secret_ingredient": "string",
        "restaurant_name": restaurant.restaurant_name
    }

    # Отправляем POST запрос и проверяем ответ
    response = client.post(reverse('add-items'), data=test_data, format='json')

    # Проверка статуса и содержимого ответа
    assert response.status_code == 201
