from django.db import models
from django.contrib.auth.hashers import make_password,check_password

class CustomAdmin(models.Model):
    email = models.EmailField(unique=True,default="placeholder@example.com")
    username=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=128)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username