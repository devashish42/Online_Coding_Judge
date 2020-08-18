
from django.urls import include, path 
from UserDetails.views import UserRegister
from rest_framework import routers


urlpatterns = [
    path('register/', UserRegister.as_view())
]