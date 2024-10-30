from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect

def admin_required(view_func):
    """Decorator to restrict access to Clients only."""
    
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id=request.session.get('user_id')
        user_type=request.session.get('user_type')
        if user_id and user_type == 'admin':
            return view_func(request, *args, **kwargs)  
        return redirect('admin_login')
    return _wrapped_view