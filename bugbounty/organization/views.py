from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseForbidden
from .forms import OrganizationLoginForm,OrganizationRegistrationForm,BountyCreationForm
from .models import Organization,Bounty
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from .decorators import org_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
# def organization_registration(request):
#     if request.method == 'POST':
#         form = OrganizationRegistrationForm(request.POST)
#         if form.is_valid():
#             org = form.save(commit=False)
#             raw_password = form.cleaned_data["password"]
#             org.password = make_password=raw_password  # Hash the password before saving
#             org.save()
#             messages.success(request, "Registration successful! Awaiting admin approval.")
#             return redirect('organization_login')
#     else:
#         form = OrganizationRegistrationForm()
#     return render(request, 'organization_signup.html', {'form': form})



# def organization_login(request):
#     if request.method == 'POST':
#         form = OrganizationLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             try:
#                 org = Organization.objects.get(email=email)
                
#                 # Debugging output
#                 print("Stored password in database:", org.password)
#                 print("Entered password:", password)
                
#                 # Directly compare passwords as plain text
#                 if password == org.password:
#                     if not org.is_approved:
#                         messages.error(request, "Access denied. Please wait for admin approval.")
#                         return redirect('organization_login')
                    
#                     # Log the user in
#                     request.session['organization_id'] = org.id
#                     request.session['user_type'] = org.user_type
#                     request.session.modified = True
#                     return redirect('organization_dashboard')
#                 else:
#                     form.add_error(None, "Invalid email or password.")
#             except Organization.DoesNotExist:
#                 form.add_error(None, "Invalid email or password.")
#     else:
#         form = OrganizationLoginForm()
#     return render(request, 'organization_login.html', {'form': form})

def org_auth(request):
    if request.method=='POST':
        login_form=OrganizationLoginForm()
        signup_form=OrganizationRegistrationForm()
        action=request.POST.get('action')
        if action == 'login':
            print('login')
            login_form=OrganizationLoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                try:
                    org = Organization.objects.get(email=email)
                    
                    
                # Debugging output
                    print("Stored password in database:", org.password)
                    print("Entered password:", password)
                
                # Directly compare passwords as plain text
                    if check_password(password,org.password):
                        print("valid")
                        if not org.is_approved:
                            messages.error(request, "Access denied. Please wait for admin approval.")
                            return redirect('org_auth')
                        request.session['organization_id'] = org.id
                        request.session['user_type'] = org.user_type
                        request.session.modified = True
                        return redirect('organization_dashboard')
                
                    else:
                        login_form.add_error(None, "Invalid email or password.")
                        print("invalid")
                except Organization.DoesNotExist:
                    login_form.add_error(None, "Invalid email or password.")
                    messages.error(request,"Invalid email or password.")
                    
                    
                    
        elif action == 'signup':
            print('signup')
            signup_form = OrganizationRegistrationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.save()
                messages.success(request,"Your account has been created successfully. Please wait for admin approval.")
                return redirect('org_auth')
    else:
        login_form = OrganizationLoginForm()
        signup_form = OrganizationRegistrationForm()
    return render(request,'org_auth.html',{'login_form': login_form,
        'signup_form': signup_form})

@org_required
def organization_dashboard(request):
    org=Organization.objects.get(id=request.session['organization_id'])
    bounties=Bounty.objects.filter(organization_id=request.session['organization_id'])
    return render(request,'organization_dashboard.html',{'org':org,'bounties':bounties})

@org_required
def add_bounty(request):
    if request.method == "POST":
        form = BountyCreationForm(request.POST)
        if form.is_valid():
            bounty = form.save(commit=False)
            print(bounty)
            scopes=request.POST.getlist('scopes[]')
            bounty.scopes=scopes
            bounty.organization = request.organization  # Link bounty to the logged-in organization
            bounty.save()
            return redirect('organization_dashboard')  # Redirect to a success page or bounty list
    else:
        form = BountyCreationForm()
    return render(request, 'add_bounty.html', {'form': form})
    


# @org_required
# def create_bounty(request):
#     if request.method == "POST":
#         form = BountyCreationForm(request.POST)
#         if form.is_valid():
#             bounty = form.save(commit=False)
#             print(bounty)
#             bounty.organization = request.organization  # Link bounty to the logged-in organization
#             bounty.save()
#             return redirect('Bounties')  # Redirect to a success page or bounty list
#     else:
#         form = BountyCreationForm()
#     return render(request, 'create_bounty.html', {'form': form})

@org_required
def bounties(request):
    if request.method =='GET':
        bounties=Bounty.objects.filter(organization_id=request.session['organization_id'])
        return render(request,'org_bounties.html',{"bounties":bounties})

@org_required
def update_bounties(request):
    if request.method =='GET':
        bounties=Bounty.objects.filter(organization_id=request.session['organization_id'])
        return render(request,'update_bounty.html',{"bounties":bounties})

@org_required
def update_bounty(request,id):
    bounty=get_object_or_404(Bounty,id=id)
    if request.method=='GET':
        form = BountyCreationForm(instance=bounty)
        return render(request,'update_view.html',{"bounty":bounty,'form':form})
    
    if request.method == "POST":
        form = BountyCreationForm(request.POST,instance=bounty)
        if form.is_valid():
            new_scopes = request.POST.getlist('scopes[]')  
            existing_scopes = bounty.scopes or []  
            updated_scopes = list(set(existing_scopes + new_scopes)) 
            bounty.scopes = updated_scopes
            form.save()
            return redirect('organization_dashboard')
    else:
        form =BountyCreationForm(instance=bounty)
    return render(request,'update_view.html',{'form':form,'bounty':bounty})    

    
    



@org_required
def delete_bounties(request):
    if request.method =='GET':
        bounties=Bounty.objects.filter(organization_id=request.session['organization_id'])
        return render(request,'delete_bounty.html',{"bounties":bounties})
    
    if request.method =='POST':
        bounty_id=request.POST.get('bounty_id')
        if bounty_id:
            bounty=get_object_or_404(Bounty,id=bounty_id,organization_id=request.session['organization_id'])
            bounty.delete()
            return redirect('organization_dashboard')
        return HttpResponseForbidden("Invalid request.")

@org_required
def program(request,slug):
    if request.method=='GET':
        program=get_object_or_404(Bounty,slug=slug)
        return render(request,'program.html',{"program":program})
    
@org_required
def logout(request):
    auth_logout(request)
    return redirect('org_auth')