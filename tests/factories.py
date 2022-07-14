import factory
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
from apis import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = fake.name()
    is_active = True
    email = fake.email()
    password = fake.password()


# class ImageFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = models.Image

#     name = 'django'