from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home-restaurant'),
    path('create/', views.add_items, name='add-restaurant'),
    path('all/', views.view_items, name='view-restaurants'),
    path('update/<slug:restaurant_slug>/', views.update_items, name='update-restaurant'),
    path('delete/<slug:restaurant_slug>/', views.delete_items, name='delete-restaurant'),
]   