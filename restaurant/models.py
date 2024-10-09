from django.db import models

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    restaurant_address = models.TextField()
  
    def __str__(self):
        return f"id - {str(self.pk)}, Name - {self.restaurant_name}"