from django import forms
from .models import Organization,Bounty

class OrganizationRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',  # Add placeholder here
            'class': 'input'         # Add your custom CSS class
        }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',  # Add placeholder here
            'class': 'input'         # Add your custom CSS class
        }))
    company_name=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Organization name',  # Add placeholder here
            'class': 'input'         # Add your custom CSS cTextInputlass
        }))
    company_website=forms.URLField(widget=forms.URLInput(attrs={
            'placeholder': 'Organization website URL',  # Add placeholder here
            'class': 'input'         # Add your custom CSS class
        }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Organization Email',
        'class':'input'
    }))
    class Meta:
        model = Organization
        fields = ['company_name','company_website','email','password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data

class OrganizationLoginForm(forms.Form):
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

class BountyCreationForm(forms.ModelForm):
    class Meta:
        model = Bounty
        fields = ['Title', 'description','url', 'min_reward', 'max_reward', 'start_date', 'end_date']
