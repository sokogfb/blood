from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blooddonors/', views.blood_donors, name='blood_donors'),
    path('donateblood/', views.donate_blood, name='donate_blood'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgotten_password/', views.forgotten_password, name='forgotten_password'),
    path('register/', views.register, name='register'),

] 