import pytest
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
from rest_framework.test import APIClient

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
    #data = response.data
    assert response.status_code == code
