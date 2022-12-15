from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


''' RETRIEVING LIST OF USERS. CAN SUBSET TO CLIENTS AND CONSULTANTS '''
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    
    if request.method == 'GET':
        condition_get = request.data['condition_get']

        if condition_get == 'everyone':
            users = User.objects.all()
            #serialize it
            serializer = UserSerializer(users, many=True)
            #return list
            return Response(serializer.data)

        elif condition_get == 'consultants':
            user_consultants = User.objects.filter(is_consultant=True)
            s= UserSerializer(user_consultants, many =True)
            test = [t.id for t in user_consultants]
            list_consultant = Consultant.objects.filter(user__in=test)
            serializer = ConsultantSerializer(list_consultant, many=True) 
            return Response({'user' : s.data,
                             'consultant' : serializer.data})
        
        elif condition_get == 'clients':
            user_clients = User.objects.filter(is_consultant=False)
            s= UserSerializer(user_clients, many =True)
            test = [t.id for t in user_clients]
            client_list = Client.objects.filter(user__in=test)
            serializer = ClientSerializer(client_list, many=True) 
            return Response({'user' : s.data,
                             'client' : serializer.data})

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "POST":
        #get the data from the request
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(pk=serializer.data['id'])
            if serializer.data['is_consultant'] == True:
                consultant = Consultant(user=user)
                consultant.save()
                return Response(serializer.data)
            elif serializer.data['is_consultant'] == False:
                client = Client(user=user)
                client.save()
                return Response(serializer.data)
        else:
            return Response({'msg':'error'})


''' RETRIEVING INFORMATION ABOUT PARTICULAR USER / CONSULTANT / CLIENT '''
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
        serializer = UserSerializer(user, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET', 'PUT', 'DELETE'])
def consultant_detail(request, id, format=None):
    try:
        consultant = Consultant.objects.get(pk=id)
    except Consultant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ConsultantSerializer(consultant)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ConsultantSerializer(consultant, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        consultant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, id, format=None):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ClientSerializer(client, data=request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


''' PROJECTS '''
@api_view(['GET', 'POST'])
def project_list(request, format=None):
    if request.method == 'GET':
        #get all users
        projects = Project.objects.all()
        #serialize it
        serializer = ProjectSerializer(projects, many=True)
        #return list
        return Response(serializer.data)
    
    if request.method == "POST":
        #get the data from the request
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'msg':'error'})

@api_view(['GET', 'PUT', 'DELETE'])
def project_details(request, id, format=None):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


''' TASKS '''
@api_view(['GET', 'POST'])
def task_list(request, format=None):
    if request.method == "GET":
        pass