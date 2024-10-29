from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from django.contrib.auth.hashers import make_password,check_password
# Registration view for UserType1
def user_signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            raw_password=form.cleaned_data['password']

            user.save()
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Email: {email}, Password: {password}")

            try:
                user = User.objects.get(email=email)
                print(f"Stored hashed password:{user.password}")
                print(f"password match:{check_password(password,user.password)}")
                
                if check_password(password, user.password):
                    
                    # Log the user in (you can use session or any other method)
                    request.session['user_id'] = user.id
                    return redirect('user_dashboard')  # Redirect to a home page
                else:
                    print("Password is incorrect")
                    # Invalid password
                    form.add_error(None, "Invalid email or password.")
            except User.DoesNotExist:
                form.add_error(None, "Invalid email or password.")
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'form': form})

def user_dashboard(request):
    return render(request,'user_dashboard.html')