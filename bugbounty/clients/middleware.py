from django.shortcuts import redirect
from django.urls import reverse

class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.user_type == 'USER':
                if 'organization' in request.path or 'admin' in request.path:
                    return redirect('user_dashboard')
            elif request.user.user_type == 'ORGANIZATION':
                if 'user' in request.path or 'admin' in request.path:
                    return redirect('organization_dashboard')
            elif request.user.is_superuser:
                if 'user' in request.path or 'organization' in request.path:
                    return redirect('admin_dashboard')
        
        response = self.get_response(request)
        return response