from django.urls import path
from . import views

urlpatterns = [
     path('signup/',views.organization_registration,name='organization_signup'),
      path('login/',views.organization_login,name='organization_login'),
      path('dashboard/',views.organization_dashboard,name='organization_dashboard'),
]