# myapp/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from clients.models import User
from organization.models import Organization
from admin_app.models import CustomAdmin
class MultiUserModelBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        # Try to authenticate as a Client
        try:
            client = User.objects.get(email=email)
            if check_password(password, client.password):
                return client
        except User.DoesNotExist:
            pass
        
        # Try to authenticate as an Organization
        try:
            organization = Organization.objects.get(email=email)
            if check_password(password, organization.password):
                return organization
        except Organization.DoesNotExist:
            pass

        try:
            admin = CustomAdmin.objects.get(email=email)
            if check_password(password, client.password):
                return client
        except CustomAdmin.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        # Check if the user exists in Client
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            pass
        
        # Check if the user exists in Organization
        try:
            return Organization.objects.get(pk=user_id)
        except Organization.DoesNotExist:
            return None
        
        try:
            return CustomAdmin.objects.get(pk=user_id)
        except CustomAdmin.DoesNotExist:
            return None
    