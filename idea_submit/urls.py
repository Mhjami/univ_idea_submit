from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('user/', include('account.urls')),
    path('login/',  include("django.contrib.auth.urls")),
    
]