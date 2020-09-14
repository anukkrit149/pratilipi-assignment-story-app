"""
Copyrights Reserved 
Developed By- Anukkrit Shanker
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('story/<int:pk>', storyDetail),
    path('story/<int:pk>/<int:userId>/api/', storyLiveViews.as_view())
]
