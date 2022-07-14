import pytest
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from PIL import Image

client = APIClient()

@pytest.mark.parametrize(
    "username, email, password, code",
    [
        ("kamakshi","kamak@gmail.com","ancd",201),
        (fake.name,"","",400),
        ("kamakshi","kamak@gmail.com","ancd",201)
    ],
)

@pytest.mark.django_db
def test_user(username, email, password, code):
    payload = dict(
        username = username,
        email = email,
        password = password
    )
    response = client.post("http://127.0.0.1:8000/users/",payload)
    assert response.status_code == code


img  = open("C:/Users/user/Desktop/Demo/poster.jpg", 'rb')
@pytest.mark.parametrize(
    "name, image, code",
    [
        ("kamakshi",img,201),
    ],
)

@pytest.mark.django_db
def test_user(user_factory, name, image, code):
    payload = dict(
        name = name,
        image = image
    )
    #user = User.objects.create_user(username = 'adk', password = 'adk')
    user = user_factory.save()
    #user.is_active = True
    #user.save()
    jwt_token = client.post("http://127.0.0.1:8000/api/token/",{"username": "adk", "password": "adk"},format='json')
    print("Token", jwt_token.data)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt_token.data['access'])
    response = client.post("http://127.0.0.1:8000/upload_image/",payload, format = 'multipart')
    assert response.status_code == code


