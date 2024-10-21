# project_dir/celery.py

import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizza_restaurants.settings")
app = Celery("pizza_restaurants")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    result_expires=3600,
)
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "pizza_deleting": {  # уникальное название задачи
        "task": 'pizza.tasks.delete_pizza_celery_schedule',  # путь к задаче
        "schedule": timedelta(minutes=1),  # интервал, через который будет выполняться задача
    },
}

if __name__ == '__main__':
    app.start()