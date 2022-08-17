from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
    
    def validate(self, attrs):
        name = attrs.get('name')
        phone = attrs.get('phone_number')
        email = attrs.get('email')
        queryset = Contact.objects.all()
        
        if len(str(phone)) != 11:
            raise serializers.ValidationError({'error':'phone number must be 11 characters'})
        
        elif Contact.objects.filter(name=name).exists():
            raise serializers.ValidationError({'error':'use another name of save contact as name already exists in the contact list'})
        elif Contact.objects.filter(phone_number=phone).exists():
            raise serializers.ValidationError({'error':'phone number already exists in the contact list'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
        
    