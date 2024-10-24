# Generated by Django 5.1.2 on 2024-10-08 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_remove_pizza_restaurant'),
        ('restaurant', '0005_remove_restaurant_restaurant_id_restaurant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
            preserve_default=False,
        ),
    ]
