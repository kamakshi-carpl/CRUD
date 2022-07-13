import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

client = APIClient()

def test_example():
    assert 1 == 1

@pytest.mark.django_db
def test_new_user(user_factory):
    user_factory.create()
    print(user_factory.password)
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_user_api():
    payload = dict(
        username = 'admi',
        email = 'admin@gmail.com',
        password = 'abcd'
    )
    response = client.post("http://127.0.0.1:8000/users/",payload)
    data = response.data
    assert data['username'] == 'admi'