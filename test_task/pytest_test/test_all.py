import pytest
from tasks.models import Task
from users.models import CustomUser
from rest_framework import status
from django.urls import reverse
 
tasks_list = 'tasks-list'
tasks_detail = 'tasks-detail'

@pytest.mark.django_db
def test_creation_task(user, api_client):
    url = reverse(tasks_list)
    data = {
        'title': 'Test task',
        'description': 'Test description',
        'due_date': '2025-02-07',
        'user': user.id
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1
    assert response.data['title'] == data['title']
    assert response.data['description'] == data['description']
    assert response.data['due_date'] == data['due_date']
    assert response.data['user'] == data['user']
    
@pytest.mark.django_db
def test_creation_user(api_client):
    url = reverse('user_create')
    data = {
        'username': 'test_user',
        'email': 'test@mail.ru'
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert CustomUser.objects.count() == 1
    assert response.data['username'] == data['username']
    assert response.data['email'] == data['email']
    

def test_get_user(api_client, user):
    url = reverse('user_detail', args=[user.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == user.username
    assert response.data['email'] == user.email

def test_get_task(api_client, task):
    url = reverse(tasks_detail, args=[task.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == task.title
    assert response.data['description'] == task.description
    assert response.data['due_date'] == task.due_date
    assert response.data['user'] == task.user.id

def test_update_task(api_client, task):
    url = reverse(tasks_detail, args=[task.id])
    data = {
        'title': 'New title',
        'description': 'New description',
        'due_date': '2025-02-07',
        'user': task.user.id
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == data['title']
    assert response.data['description'] == data['description']
    assert response.data['due_date'] == data['due_date']
    assert response.data['user'] == data['user']

def test_get_tasks_for_user(api_client, user, task):
    url = reverse(tasks_list)
    response = api_client.get(url, {'user': user.id})
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['title'] == task.title
    assert response.data[0]['description'] == task.description
    assert response.data[0]['due_date'] == task.due_date
    assert response.data[0]['user'] == task.user.id
    assert response.data[0]['user'] == user.id

def test_delete_task(api_client, task):
    url = reverse(tasks_detail, args=[task.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.count() == 0

