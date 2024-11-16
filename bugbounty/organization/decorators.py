from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps
from .models import Organization  # Import your Organization model

def org_required(view_func):
    """Decorator to restrict access to Organizations only."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        org_id = request.session.get('organization_id')
        user_type = request.session.get('user_type')

        if org_id and user_type == 'organization':
            try:
                # Fetch the organization and attach it to the request
                request.organization = Organization.objects.get(pk=org_id)
            except Organization.DoesNotExist:
                return redirect('org_auth')  # Redirect if organization not found
            
            return view_func(request, *args, **kwargs)
        
        # Redirect to login page if user isn't authenticated as 'organization'
        return redirect('org_auth')

    return _wrapped_view
