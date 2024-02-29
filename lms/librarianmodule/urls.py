from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
        path('bookpost', views.bookpost, name='bookpost'),
        path('adddbook',views.add_book, name='addbook'),
        path('viewbooks', views.view_books, name='view_books'),
]