from django.contrib import admin
from django.urls import path, include
from . import views
from .views import view_book

urlpatterns = [

    path('genre',views.genre, name='genre'),
    path('books', view_book, name='view_book'),
    path('logout/', views.logout_view, name='logout'),
]