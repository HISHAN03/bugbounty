from django.shortcuts import render, redirect
from .forms import OrganizationLoginForm,OrganizationRegistrationForm,BountyCreationForm
from .models import Organization,Bounty
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from .decorators import org_required
from django.contrib import messages

def organization_registration(request):
    if request.method == 'POST':
        form = OrganizationRegistrationForm(request.POST)
        if form.is_valid():
            org = form.save(commit=False)
            raw_password = form.cleaned_data["password"]
            org.password = make_password=raw_password  # Hash the password before saving
            org.save()
            messages.success(request, "Registration successful! Awaiting admin approval.")
            return redirect('organization_login')
    else:
        form = OrganizationRegistrationForm()
    return render(request, 'organization_signup.html', {'form': form})



def organization_login(request):
    if request.method == 'POST':
        form = OrganizationLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                org = Organization.objects.get(email=email)
                
                # Debugging output
                print("Stored password in database:", org.password)
                print("Entered password:", password)
                
                # Directly compare passwords as plain text
                if password == org.password:
                    if not org.is_approved:
                        messages.error(request, "Access denied. Please wait for admin approval.")
                        return redirect('organization_login')
                    
                    # Log the user in
                    request.session['organization_id'] = org.id
                    request.session['user_type'] = org.user_type
                    request.session.modified = True
                    return redirect('organization_dashboard')
                else:
                    form.add_error(None, "Invalid email or password.")
            except Organization.DoesNotExist:
                form.add_error(None, "Invalid email or password.")
    else:
        form = OrganizationLoginForm()
    return render(request, 'organization_login.html', {'form': form})


@org_required
def organization_dashboard(request):
    return render(request,'organization_dashboard.html')

@org_required
def create_bounty(request):
    if request.method == "POST":
        form = BountyCreationForm(request.POST)
        if form.is_valid():
            bounty = form.save(commit=False)
            print(bounty)
            bounty.organization = request.organization  # Link bounty to the logged-in organization
            bounty.save()
            return redirect('Bounties')  # Redirect to a success page or bounty list
    else:
        form = BountyCreationForm()
    return render(request, 'create_bounty.html', {'form': form})

@org_required
def bounties(request):
    if request.method =='GET':
        bounties=Bounty.objects.all()

        return render(request,'org_bounties.html',{"bounties":bounties})
