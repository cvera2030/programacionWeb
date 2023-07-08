from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('galeria/', views.galeria, name='gallery-page'),
    path('about-us/', views.aboutUs, name='about-us-page'),
    path('login-page/', views.loginPage, name='login-page'),
]
