import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atomic_habits.settings')

app = Celery('atomic_habits')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем задачи в установленных приложениях
app.autodiscover_tasks()
