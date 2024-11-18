from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect

def client_required(view_func):
    """Decorator to restrict access to Clients only."""
    
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id=request.session.get('user_id')
        user_type=request.session.get('user_type') 
        if user_id and user_type == 'user':
            return view_func(request, *args, **kwargs)
             
        return redirect('user_auth')
    return _wrapped_view
