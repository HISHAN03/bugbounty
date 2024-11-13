from django.urls import path
from . import views

urlpatterns = [
        path('login/',views.admin_login,name='admin_login'),
        path('signup/',views.admin_signup,name='admin_signup'),
        path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
        path('approve_organization/<int:org_id>/', views.approve_organization, name='approve_organization'),
        path('dashboard/users/',views.users,name='user_list'),
        path('dashboard/approval_requests/',views.pending_requests,name='approval_requests'),
        path('dashboard/organizations/',views.organizations,name='orgs_list')
]
