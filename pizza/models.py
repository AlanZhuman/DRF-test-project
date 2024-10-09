from django.db import models
from restaurant.models import Restaurant

class Pizza(models.Model):
    class Dough_type(models.TextChoices):
        THIN = 'THIN', 'THIN'
        THICK = 'THICK', 'THICK'

    pizza_name = models.CharField(max_length=100)
    cheese_type = models.CharField(max_length=50)
    dough_type = models.CharField(choices=Dough_type.choices ,max_length=50)
    secret_ingredient = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, related_name='pizzas', on_delete=models.CASCADE)

    def __str__(self):
        return f"id - {str(self.pk)}, Name - {self.pizza_name}"