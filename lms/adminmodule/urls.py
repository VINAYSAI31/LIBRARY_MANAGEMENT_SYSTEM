from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),

    path('user', views.userhomepage, name='userhomepage'),
    path('lib',views.libhomepage,name='libhomepage'),

    path('login',views.loginpage,name='loginpage'),
    path('login1',views.login1,name='login1'),
    path('signup',views.register,name='register'),
    path('signup1',views.signup1,name='register1'),
    path('location',views.locationpage,name='location'),
path('feedback',views.feedback, name='feedback'),
    path('send_feedback', views.send_feedback, name='send_feedback'),
    path('sucess', views.success, name='sucess'),

]