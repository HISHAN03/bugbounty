from django import forms
from .models import CustomAdmin

class AdminLoginForm(forms.ModelForm):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())