from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Custom logout page must come before auth urls
    path('logout/', views.logout_view, name='logout'),
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
    
    path('register/', views.register, name='register'),
]