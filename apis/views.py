from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .serializers import ImageSerializer, UserSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import User, Image
from rest_framework.parsers import JSONParser
from django.http import QueryDict
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        print(serializer)
        if serializer.is_valid() and request.POST['username'] and request.POST['password']:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_images(request):
    permission_classes = (IsAuthenticated,)
    user = request.user.id
    if request.method == 'GET': 
        images = Image.objects.filter(user_id = user)
        image_serializer = ImageSerializer(images, many = True)
        return Response(image_serializer.data) 

@api_view(['POST'])
def upload_image(request):
    permission_classes = (IsAuthenticated,)
    user = request.user.id
    print(request.FILES)
    serializer = ImageSerializer(data = {'name' : request.POST['name'], 'image' : request.FILES['image'], 'user_id' : user})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def modify_image(request, id):
    try: 
        image_object = Image.objects.get(id=id) 
    except Image.DoesNotExist: 
        return JsonResponse({'message': 'The image does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'PUT': 
        image_serializer = ImageSerializer(image_object, data=request.data) 
        if image_serializer.is_valid(): 
            image_serializer.save() 
            return JsonResponse(image_serializer.data) 
        return JsonResponse(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        if image_object.image:
            image_object.image.delete()
        image_object.delete() 
        return JsonResponse({'message': 'Image was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def sign_up():
    serializer = UserSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def test():
    return Response({'abc': 9}, status=status.HTTP_400_BAD_REQUEST)