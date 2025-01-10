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
    Title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Title',  # Add placeholder here
            'class': 'form-control',
            'value': '',        # Add your custom CSS class
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'description',  # Add placeholder here
            'class': 'form-control'         # Add your custom CSS class
        })
    )
    scopes = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'https://example.com',  # Add placeholder here
            'class': 'form-control',
            
                     # Add your custom CSS class
        }),
        required=False
    )
    min_reward = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Minimum Reward',  # Add placeholder here
            'class': 'form-control',
            'value':0,             
        })
    )
    max_reward = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Maximum Reward',  # Add placeholder here
            'class': 'form-control',
            'value':0, 
        })
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'placeholder': 'Start Date',  
            'class': 'form-control',
            'type':'date',                      
              })
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'placeholder': 'End date',  
            'class': 'form-control',
            'type':'date',         
        })
    )
    class Meta:
        model = Bounty
        fields = ['Title', 'description','scopes', 'min_reward', 'max_reward', 'start_date', 'end_date']
