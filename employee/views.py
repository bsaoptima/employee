from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


''' Retrieving users '''

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        #get all users
        users = User.objects.all()
        #serialize it
        serializer = UserSerializer(users, many=True)
        #return list
        return Response(serializer.data)
    
    if request.method == "POST":
        #get the data from the request
        serializer = UserSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

''' Get details of a single user '''

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)