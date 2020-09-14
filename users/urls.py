"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', signup, name='Signup'),
    path('', auth_views.LoginView.as_view(template_name='detail/login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='detail/login.html'), name='Logout'),
]