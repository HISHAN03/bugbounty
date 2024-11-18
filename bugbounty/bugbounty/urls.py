from django.contrib import admin
from django.urls import path, include
from clients.views import landing_page
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/', include('clients.urls')),
    path('organization/', include('organization.urls')),
    path('admin/', include('admin_app.urls')),
    path('',landing_page,name='landing_page')
]
