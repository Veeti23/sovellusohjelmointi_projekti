from django.urls import path, include
from . import views
from .views import CustomLoginView

app_name = 'users'
urlpatterns = [
    # Custom login page must come before auth urls
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    # Include default auth urls last
    path('', include('django.contrib.auth.urls')),
]