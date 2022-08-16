from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(max_length=255,null=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255,null=True)
    occupation = models.CharField(max_length=255,null=True)
    relationship = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return f"{self.name} : {self.occupation}"
    
    class Meta:
        ordering = ['name']