from django.db import models
from django.contrib.auth.hashers import make_password, check_password

    
class Organization(models.Model):
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store the password in plain text
    is_approved = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, default='organization')

    def __str__(self):
        return self.company_name


class Bounty(models.Model):
    # company=models.ForeignKey(Organization,related_name='bounties',on_delete=models.CASCADE,null=True)
    Title=models.CharField(max_length=255,blank=False)
    description=models.TextField()
    min_reward = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Minimum reward amount")
    max_reward = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Maximum reward amount")
    status=models.BooleanField(default=True)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.title