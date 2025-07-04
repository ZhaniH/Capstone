from django.contrib import admin
from django.urls import path, include
from TinyBubbles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TinyBubbles.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('tour/', views.tour_dates, name='tour'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]