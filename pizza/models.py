from django.db import models
from restaurant.models import Restaurant
from django.urls import reverse
from django.template.defaultfilters import slugify

class Pizza(models.Model):
    class Dough_type(models.TextChoices):
        THIN = 'THIN', 'THIN'
        THICK = 'THICK', 'THICK'

    pizza_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default=None)
    cheese_type = models.CharField(max_length=50)
    dough_type = models.CharField(choices=Dough_type.choices ,max_length=50)
    secret_ingredient = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, related_name='pizzas', on_delete=models.CASCADE)

    def __str__(self):
        return f"Pizza name - {self.pizza_name}"
    
    def get_absolute_url(self):
        return reverse('pizza', kwargs={'pizza_slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.pizza_name)
        super(Pizza, self).save(*args, **kwargs)