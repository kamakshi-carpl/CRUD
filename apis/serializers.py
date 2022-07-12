from rest_framework import serializers
from .models import Image, User

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name', 'image', 'user_id', 'id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')