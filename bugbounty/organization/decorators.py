# decorators.py
from django.http import HttpResponseForbidden
from functools import wraps
from .utils import is_organization

def organization_required(view_func):
    """Decorator to restrict access to Organizations only."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not is_organization(request.user):
            return HttpResponseForbidden("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
