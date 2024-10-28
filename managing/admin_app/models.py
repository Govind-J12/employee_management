from django.db import models

# Create your models here.

class addemployee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    date_joined = models.DateField()
    
    
    
    
    
    
