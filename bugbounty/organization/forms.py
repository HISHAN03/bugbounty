from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Organization

class OrganizationRegistrationForm(UserCreationForm):
    class Meta:
        model=Organization
        fields=['company_name','company_website','password1','password2']

class OrganizationLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )