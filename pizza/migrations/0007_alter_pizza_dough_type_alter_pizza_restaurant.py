# Generated by Django 5.1.2 on 2024-10-09 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_alter_pizza_dough_type'),
        ('restaurant', '0005_remove_restaurant_restaurant_id_restaurant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='dough_type',
            field=models.CharField(choices=[('THIN', 'THIN'), ('THICK', 'THICK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='restaurant.restaurant'),
        ),
    ]
