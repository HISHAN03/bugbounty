from django.db import models
from django.contrib.auth.models import AbstractUser
class Organization(AbstractUser):
    company_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    company_website=models.URLField(blank=True)
    is_approved=models.BooleanField(default=False)

    username = models.CharField(max_length=150, unique=True, default="default_username")

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='organization_user_set',  # Unique related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='organization_user_permission_set',  # Unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


    def __str__(self):
        return self.company_name