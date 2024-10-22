from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-pizza'),
    path('create/delayed/', views.add_items_delayed, name='add-pizza-delayed'),
    path('all/', views.view_items, name='view-pizzas'),
    path('update/<slug:pizza_slug>/', views.update_items, name='update-pizza'),
    path('delete/<slug:pizza_slug>/', views.delete_items, name='delete-pizza'),
]   