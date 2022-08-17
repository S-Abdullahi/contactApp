from tkinter.ttk import Style
from rest_framework import serializers
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'password2']
        
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        
        if len(password) < 6:
            raise serializers.ValidationError({'error': "minimum number of character is 6"})
        
        if password != password2:
            raise serializers.ValidationError({'error': 'password 1 and password2 must be equal'})
        return super().validate(attrs)


    def save(self, **kwargs):
        username = self.validated_data['username']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error': 'username already exists'})
        
        account = User(username=username, first_name=first_name, last_name=last_name)
        account.set_password(password)
        account.save()
        
        return account
    


        
    #     return super().save(**kwargs)
        