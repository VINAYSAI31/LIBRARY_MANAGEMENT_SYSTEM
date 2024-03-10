from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('genre',views.genre, name='genre'),



path('logout/', views.logout_view, name='logout'),
]