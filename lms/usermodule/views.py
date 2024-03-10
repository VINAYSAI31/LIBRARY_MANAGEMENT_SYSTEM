from django.shortcuts import render
from .models import  *

from django.contrib.auth import logout
from django.contrib import messages






# Create your views here.

def genre(request):
    return render(request,'user/genre.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return render(request, 'homepage.html')


def view_books(request):
    book_details_list=BookDetails.objects.all()
    return render(request,'user/viewbook.html',{'book_details_list':book_details_list})



