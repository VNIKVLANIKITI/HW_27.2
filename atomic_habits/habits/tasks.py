from celery import shared_task
from link_telegramm.views import send_telegram_message
from datetime import datetime
from django.conf import settings
import requests
from celery import shared_task
from django.urls import reverse
from django.conf import settings


@shared_task
def send_reminder(habit_id, message_text):
    print('Отправим напоминание')

    base_url = settings.BASE_URL 
    print(f"Base URL: {base_url}")
    send_message_url = f"{base_url}{reverse('link_telegramm:send_message')}"
    print(f"Send message URL: {send_message_url}")

    # Подготовка данных для отправки (текст сообщения)
    payload = {
        "text": message_text  # Текст сообщения, передаваемый в контроллер
    }

    try:
        # Отправка POST-запроса с текстом сообщения
        response = requests.post(send_message_url, json=payload)
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
    except Exception as e:
        print(f"Error occurred: {e}")