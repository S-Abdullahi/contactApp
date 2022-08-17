from urllib import request
from rest_framework import permissions

class IsContactOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.User == request.user or request.user == request.user.is_staff
    
    