from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Organization(models.Model):
    company_name=models.CharField(max_length=255)
    company_website=models.URLField(blank=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    is_approved=models.BooleanField(default=False)
    user_type=models.CharField(max_length=20,default='organization')
    def save(self,*args,**kwargs):
        self.password=make_password(self.password)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.company_name

class Bounty(models.Model):
    Title=models.CharField(max_length=255,blank=False)
    description=models.TextField()
    status=models.BooleanField(default=True)
    start_date=models.DateField()
    end_date=models.DateField()