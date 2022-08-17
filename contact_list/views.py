from imp import get_magic
from django.shortcuts import render
from .models import Contact
from .serializer import ContactSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from rest_framework import filters
from . import permission
# Create your views here.

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','relationship','occupation','address']
    

    

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permission.IsContactOwner]
    

