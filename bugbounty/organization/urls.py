from django.urls import path
from . import views

urlpatterns = [
      # path('signup/',views.organization_registration,name='organization_signup'),
      # path('login/',views.organization_login,name='organization_login'),
      path('dashboard/',views.organization_dashboard,name='organization_dashboard'),
      path('dashboard/Bounties',views.bounties,name='Bounties'),
      path('dashboard/Update-Bounties',views.update_bounties,name='update_bounty'),
      path('auth/',views.org_auth,name='org_auth'),
      # path('dashboard/Add-Bounty',views.create_bounty,name='create_bounty'),
      path('dashboard/add_bounty',views.add_bounty,name='add_bounty'),
      path('dashboard/program/<slug:slug>',views.program,name='program'),
      path('logout/', views.logout, name='org_logout'),
      
]