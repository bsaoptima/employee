from django.db import models
from django.urls import reverse

# Create your models here.pi



class User(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique= True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    isemailvalid = models.BooleanField(default = False) # for later to verify email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class SignUpToken(models.Model) :
    # for later 
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()


class Consultant(models.Model):
    
    ''' 
    Consultant Class 
    -Who they are
    -The team they are in (figure out the foreign keys)
    
    Connections:
    -Department() : One to Many
    -Team() : One to Many
    '''
    
    #Fields
    department_name = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, default="Unassigned")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #Metadata
    #class Meta:
       #ordering = ['last_name', 'first_name']
    
    #Methods
    def __str__(self):
        '''String for Representing the Model Object.'''
        return f'{self.last_name}, {self.first_name}'
    

class Department(models.Model):
    
    '''
    Department Class
    -Can be used to describe the area where a consultant works
    
    Connections:
    -Consultant() : One to One in this direction
    '''
    
    #Fields
    department_name = models.CharField(max_length=100)
    
    #Methods
    def __str__(self):
        '''String for Representing the Model Object.'''
        return self.department_name
    

class Team(models.Model):
    
    '''
    In which team is the consultant working
    
    FIGURE OUT THE FOREIGN KEYS
    
    Connections:
    -Consultant() : One to One in this direction
    '''
    
    #Fields
    team_name = models.CharField(max_length=100)
    team_project = models.OneToOneField('Project', on_delete=models.SET_NULL, null=True)

    #Methods
    def __str__(self):
        return self.team_name


class Project(models.Model):
    
    #Fields
    project_name = models.CharField(max_length=100)
    project_client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    project_description = models.TextField(max_length=200)
    project_startDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    project_endDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.project_name


class Client(models.Model):
    
    #Fields
    client_primary_contact = models.CharField(max_length=100)
    client_number_of_projects = models.IntegerField() #how many projects have we completed with this client
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 

    def __str__(self):
        return self.client_name