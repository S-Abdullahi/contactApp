from imp import get_magic
from django.shortcuts import render
from .models import Contact
from .serializer import ContactSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

# Create your views here.

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    

