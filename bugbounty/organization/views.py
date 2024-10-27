from django.shortcuts import render,redirect
from .forms import OrganizationRegistrationForm,OrganizationLoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Organization
def organization_registration(request):
    if request.method=='POST':
        form=OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_login')
    else:
        form=OrganizationRegistrationForm()
        return render(request,'organization_signup.html',{'form':form})
    
def organization_login(request):
    form=OrganizationLoginForm(request.POST or None)
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,username=email,password=password)

        if user is not None and isinstance(user,Organization):
            login(request, user)
            return redirect('organization_dashboard')  # Redirect to the organization's dashboard
        else:
            form.add_error(None, "Invalid email or password")
    return render(request, 'organization_login.html', {'form': form})


def organization_logout(request):
    logout(request)
    return redirect('organization_login')