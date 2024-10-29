from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm,AdminLoginForm
from .models import CustomAdmin
from django.contrib.auth.hashers import make_password,check_password
# Registration view for UserType1
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
            print(f"Email: {email}, Password: {password}")

            try:
                user = CustomAdmin.objects.get(email=email)
                print(f"Stored hashed password:{user.password}")
                print(f"password match:{check_password(password,user.password)}")
                
                if check_password(password, user.password):
                    
                    # Log the user in (you can use session or any other method)
                    request.session['user_id'] = user.id
                    return redirect('admin_dashboard')  # Redirect to a home page
                else:
                    print("Password is incorrect")
                    # Invalid password
                    form.add_error(None, "Invalid email or password.")
            except CustomAdmin.DoesNotExist:
                form.add_error(None, "Invalid email or password.")
    else:
        form = AdminLoginForm()
    return render(request, 'admin_login.html', {'form': form})

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')