from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<slug:pizza_slug>/', views.update_items, name='update-items'),
    path('delete/<slug:pizza_slug>//', views.delete_items, name='delete-items'),
]   