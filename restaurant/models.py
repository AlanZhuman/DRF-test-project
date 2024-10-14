from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default=None)
    restaurant_address = models.TextField()
  
    def __str__(self):
        return self.restaurant_name
    
    def get_absolute_url(self):
        return reverse('restaurant', kwargs={'restaurant_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.restaurant_name)
        super(Restaurant, self).save(*args, **kwargs)