from django.shortcuts import render
from .serializer import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from . import models
# Create your views here.

@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            
            data['response'] = 'registration is succesful'

            data['username'] = account.username
            data['email'] = account.email
            
            return Response(serializer.data)
        
        else:
            data = serializer.errors
            
        
        return Response(data, status=status.HTTP_201_CREATED)