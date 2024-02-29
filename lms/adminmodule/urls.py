from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),

    path('user', views.userhomepage, name='userhomepage'),
    path('lib',views.libhomepage,name='libhomepage'),

    path('login',views.loginpage,name='loginpage'),
    path('signup',views.register,name='register'),
    path('location',views.locationpage,name='location'),
]