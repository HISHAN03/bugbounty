from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/', include('clients.urls')),
    path('organization/', include('organization.urls')),
    path('admin/', include('admin_app.urls')),
]
