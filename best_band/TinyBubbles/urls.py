from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views

app_name = "TinyBubbles"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('tour/', views.tour_dates, name='tour'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.login_view, name='signup'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]