from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps

def org_required(view_func):
    """Decorator to restrict access to Organizations only."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        org_id = request.session.get('organization_id')
        user_type = request.session.get('user_type')

        if org_id and user_type == 'organization':
            return view_func(request, *args, **kwargs)
        
        # Redirect to login page if user isn't authenticated as 'organization'
        return redirect('organization_login')

    return _wrapped_view
