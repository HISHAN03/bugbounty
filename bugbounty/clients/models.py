from typing import Iterable
from django.db import models
from django.contrib.auth.hashers import make_password,check_password
class User(models.Model):
    email=models.EmailField(unique=True)
    username=models.CharField(unique=True,max_length=255)
    password=models.CharField(max_length=128)

    def save(self,*args,**kwargs):
        self.password=make_password(self.password)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name