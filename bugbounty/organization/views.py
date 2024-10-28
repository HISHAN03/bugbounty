from django.shortcuts import render, redirect
from .forms import OrganizationLoginForm,OrganizationRegistrationForm
from .models import Organization
from django.contrib.auth.hashers import make_password,check_password
# Registration view for UserType1
def organization_registration(request):
    if request.method == 'POST':
        form = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(form.cleaned_data["password"])
            user.save()
            return redirect('organization_login')
    else:
        form = OrganizationRegistrationForm()
    return render(request, 'organization_signup.html', {'form': form})

# Login view for UserType1
def organization_login(request):
    if request.method == 'POST':
        form = OrganizationLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Organization.objects.get(email=email)
                if check_password(password, user.password):
                    # Log the user in (you can use session or any other method)
                    request.session['user_id'] = user.id
                    return redirect('organization_dashboard')  # Redirect to a home page
                else:
                    # Invalid password
                    form.add_error(None, "Invalid email or password.")
            except Organization.DoesNotExist:
                form.add_error(None, "Invalid email or password.")
    else:
        form = OrganizationLoginForm()
    return render(request, 'organization_login.html', {'form': form})

def organization_dashboard(request):
    return render(request,'organization_dashboard.html')