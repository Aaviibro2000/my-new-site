from django.urls import path
from .views import register
from django.contrib.auth import views as authentication_views

app_name = 'users'



urlpatterns = [
    path('register/',register,name='products'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html')),
    
    
]
