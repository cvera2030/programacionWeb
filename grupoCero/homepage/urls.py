from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('galeria/', views.galeria, name='gallery_page'),
    path('about-us/', views.aboutUs, name='about-us_page'),
    path('login-page/', views.loginPage, name='login_page'),
    path('login_user/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
