from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
