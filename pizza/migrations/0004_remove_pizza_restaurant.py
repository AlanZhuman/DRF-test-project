# Generated by Django 5.1.2 on 2024-10-08 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_pizza_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='restaurant',
        ),
    ]
