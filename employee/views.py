from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


''' USERS '''

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
            consultants = User.objects.filter(is_consultant=True).first()
            consultants2 = Consultant.objects.filter(user = consultants.id).first()
            #serialize it
            serializer_user = UserSerializer(consultants)
            serializer_consultant = ConsultantSerializer(consultants2)
            #return list
            return Response({'user': serializer_user.data['name'],
                             'consultant': serializer_consultant.data})
            
        elif condition_get == 'clients':
            clients = User.objects.filter(is_consultant=False).first()
            clients2 = Client.objects.filter(user = clients.id).first()
            serializer_user = UserSerializer(clients)
            serializer_client = ClientSerializer(clients2)
            return Response({'user': serializer_user.data['name'],
                             'client' : serializer_client.data})
        
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
    

''' PROJECTS '''
'''
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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def project_user(request, id, format=None):
    try:
        project = Project.objects.get(pk=id)
    except Consultant.DoesNotExist:
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
'''