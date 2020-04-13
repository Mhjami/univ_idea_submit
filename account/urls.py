from . import views
from django.urls import path,include

urlpatterns = [
    path('register/', views.register, name='register'),
    path('',  include("django.contrib.auth.urls")),
    
]