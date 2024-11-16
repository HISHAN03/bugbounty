from django import forms
from .models import CustomAdmin

class AdminRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomAdmin
        fields = ['email', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data

class AdminLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',  # Add placeholder here
            'class': 'input'         # Add your custom CSS class
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',  # Add placeholder here
            'class': 'input'            # Add your custom CSS class
        })
    )
