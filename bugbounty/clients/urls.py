from django.urls import path
from . import views

urlpatterns = [
     path('signup/', views.user_signup, name='user_signup'),
     path('login/',views.user_login,name='user_login'),
     path('dashboard/',views.user_dashboard,name='user_dashboard'),
]