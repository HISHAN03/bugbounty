from django.shortcuts import render, redirect,get_object_or_404
from .forms import AdminRegistrationForm,AdminLoginForm
from .models import CustomAdmin
from clients.models import User
from django.contrib.auth.hashers import make_password,check_password
from organization.models import Organization
from .decorators import admin_required

def admin_signup(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            raw_password=form.cleaned_data['password']

            user.save()
            return redirect('admin_login')
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_signup.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print("eee")

            try:
                user = CustomAdmin.objects.get(email=email)
                
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    request.session['user_type']=user.user_type
                    request.session.modified=True
                    return redirect('admin_dashboard')  
                else:
                    
                    form.add_error(None, "Invalid email or password.")
            except CustomAdmin.DoesNotExist:
                form.add_error(None, "Invalid email or password.")
    else:
        form = AdminLoginForm()
    return render(request, 'admin_auth.html', {'form': form})


@admin_required
def admin_dashboard(request): 
    return render(request,'admin_dashboard.html')

@admin_required
def pending_requests(request):
    approval_requests=Organization.objects.filter(is_approved=False)
    return render(request,'approval_requests.html',{'approval_requests':approval_requests})

@admin_required
def approve_organization(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    organization.is_approved = True
    organization.save()
    return redirect('admin_dashboard')

@admin_required
def users(request):
    users=User.objects.all()
    return render(request,'user_list.html',{'users':users})

@admin_required
def organizations(request):
    orgs=Organization.objects.all()
    return render(request,'organization_list.html',{'orgs':orgs})