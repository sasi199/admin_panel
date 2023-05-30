from django.db import models

# Create your models here.
class RegisterField(models.Model):
    username=models.CharField(max_length=10)
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)
    
    
    class Meta:
       db_table='super_user'

