
import pytest
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")  # Замени "test_task" на название твоего проекта
django.setup()
from tasks.models import Task
from rest_framework.test import APIClient

@pytest.fixture
def user(django_user_model):
    user = django_user_model.objects.create(
        username='test_user',
        email='test@mail.ru'
        )
    return user

@pytest.fixture
def task(user):
    task = Task.objects.create(
        title='Test task',
        description='Test description',
        due_date='2025-02-07',
        user=user
        )
    return task

@pytest.fixture
def api_client():
    return APIClient()