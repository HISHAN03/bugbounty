from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from .decorators import client_required

# def user_signup(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             raw_password=form.cleaned_data['password']

#             user.save()
#             return redirect('user_login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'user_signup.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             try:
#                 user = User.objects.get(email=email)
#                 if check_password(password, user.password):
#                     # Log the user in (you can use session or any other method)
#                     request.session['user_id'] = user.id
#                     request.session['user_type'] = user.user_type
#                     request.session.modified = True
#                     return redirect('user_dashboard')  # Redirect to the dashboard
#                 else:
#                     # Invalid password
#                     form.add_error(None, "Invalid email or password.")
#             except User.DoesNotExist:
#                 # Invalid email
#                 form.add_error(None, "Invalid email or password.")
#     else:
#         form = UserLoginForm()  # Initialize an empty form for GET requests

#     # Always pass the form to the template
#     return render(request, 'login.html', {'form': form})

def user_auth_page(request):
    if request.method == 'POST':
        login_form = UserLoginForm()
        signup_form = UserRegistrationForm()
        action=request.POST.get('action')
        if action =='login':
            print('loginasdadaaasa')
            login_form = UserLoginForm(request.POST)
            if login_form.is_valid():
                print('valid form')
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                try:
                    print('entered try block')
                    user = User.objects.get(email=email)
                    if check_password(password, user.password):
                        # Log the user in
                        request.session['user_id'] = user.id
                        request.session['user_type'] = user.user_type
                        print("User logged in:", request.session.get('user_id'))
                        return redirect('user_dashboard')
                    else:
                        print("ibvasdasdsas")
                        login_form.add_error(None, "Invalid email or password.")
                except User.DoesNotExist:
                    login_form.add_error(None, "Invalid email or password.")
        elif action =='signup':
            signup_form = UserRegistrationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.save()
                return redirect('user_auth')
        
    else:
        login_form = UserLoginForm()
        signup_form = UserRegistrationForm()

    # Ensure both forms are passed to the template
    return render(request, 'user_auth_page.html', {
        'login_form': login_form,
        'signup_form': signup_form
    })


@client_required
def user_dashboard(request):
    return render(request,'user_dashboard.html')

# def signup(request):
#     return render(request,'login.html')

def landing_page(request):
    return render(request,'landing_page.html')