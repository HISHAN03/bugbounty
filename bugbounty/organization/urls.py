from django.urls import path
from . import views

urlpatterns = [
     path('signup/',views.organization_registration,name='org_signup'),
      path('login/',views.organization_login,name='org_login'),
]