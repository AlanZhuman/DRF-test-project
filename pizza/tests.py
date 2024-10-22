import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Restaurant
from .models import Pizza

# /api/pizza/create correct test-case
@pytest.mark.django_db
def test_create_pizza():
    # Создаем ресторан в БД
    restaurant = Restaurant.objects.create(restaurant_name="Test Restaurant", slug='test-restaurant', restaurant_address='Test Address')

    client = APIClient()
    test_data = {
        "pizza_name": "test_name",
        "cheese_type": "test_cheese",
        "dough_type": "THIN",
        "secret_ingredient": "test_ingredient",
        "restaurant_name": restaurant.restaurant_name
    }

    # Отправляем POST запрос и проверяем ответ
    response = client.post(reverse('add-pizza'), data=test_data, format='json')

    # Проверка статуса и содержимого ответа
    assert response.status_code == 201

# /api/pizza/all correct test-case
@pytest.mark.django_db
def test_view_all_pizzas():
    test_create_pizza()

    client = APIClient()
    test_data = {
        "pizza_name": "test_name_2",
        "cheese_type": "test_cheese_2",
        "dough_type": "THIN",
        "secret_ingredient": "test_ingredient_2",
        "restaurant_name": "Test Restaurant"
    }

    # Отправляем POST запрос и проверяем ответ
    response = client.post(reverse('add-pizza'), data=test_data, format='json')
    
    # Проверка статуса и содержимого ответа
    assert response.status_code == 201

    view_response = client.get(reverse('view-pizzas'))

    assert view_response.status_code == 200


# /api/pizza/update/pizza-slug correct test-case
@pytest.mark.django_db
def test_update_pizza():
    # Создаем ресторан
    another_restaurant = Restaurant.objects.create(restaurant_name="Test Another Restaurant", slug='test-another-restaurant', restaurant_address='Test Another Address')
    client = APIClient()
    test_create_pizza()

    # Получаем сгенерированный slug из ответа или напрямую из базы данных
    pizza = Pizza.objects.get(pizza_name="test_name")
    pizza_slug = pizza.slug  # Используем сгенерированный slug
    assert Pizza.objects.filter(slug=pizza_slug).exists()

    

    # Подготовка данных для обновления
    test_updated_data = {
        "pizza_name": "updated_test_name",
        "cheese_type": "updated_test_cheese",
        "dough_type": "THIN",
        "secret_ingredient": "updated_test_ingredient",
        "restaurant_name": another_restaurant.restaurant_name
    }

    # Отправляем POST запрос на обновление пиццы с использованием правильного slug
    update_response = client.post(reverse('update-pizza', args=[pizza_slug]), data=test_updated_data, format='json')

    # Проверяем успешность обновления
    assert update_response.status_code == 200

# /api/pizza/delete/pizza-slug correct test-case
@pytest.mark.django_db
def test_delete_pizza():
    # Создаем ресторан
    restaurant = Restaurant.objects.create(restaurant_name="Test Restaurant", slug='test-restaurant', restaurant_address='Test Address')

    client = APIClient()

    # Загружаем тестовые данные
    test_data = {
        "pizza_name": "test_name",
        "cheese_type": "test_cheese",
        "dough_type": "THIN",
        "secret_ingredient": "test_ingredient",
        "restaurant_name": restaurant.restaurant_name
    }

    # Отправляем POST запрос и проверяем ответ
    response = client.post(reverse('add-pizza'), data=test_data, format='json')

    # Проверяем статус создания пиццы
    assert response.status_code == 201

    # Получаем сгенерированный slug из ответа или напрямую из базы данных
    pizza = Pizza.objects.get(pizza_name="test_name")
    pizza_slug = pizza.slug  # Используем сгенерированный slug
    assert Pizza.objects.filter(slug=pizza_slug).exists()

    delete_response = client.delete(reverse('delete-pizza', args=[pizza_slug]))

    assert delete_response.status_code == 204