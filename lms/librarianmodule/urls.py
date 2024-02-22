from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
        path('bookpost', views.bookpost, name='bookpost'),
        path('adddbook',views.add_book, name='addbook'),
]