from django.shortcuts import redirect
from functools import wraps
from django.contrib import messages

def user_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 'USER':
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Unauthorized access.')
            return redirect('home')
    return wrap

def organization_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 'ORGANIZATION':
            if request.user.is_approved:
                return function(request, *args, **kwargs)
            else:
                return redirect('pending_approval')
        else:
            messages.error(request, 'Unauthorized access.')
            return redirect('home')
    return wrap

def admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            messages.error(request, 'Unauthorized access.')
            return redirect('home')
    return wrap