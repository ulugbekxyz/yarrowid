from django.urls import path
from .views import ProfileView, register, verify_account

urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', verify_account, name='verify_account'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
