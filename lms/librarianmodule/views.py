from django.shortcuts import render
from pyexpat.errors import messages

from .models import  *

# Create your views here.
def bookpost(request):
    return render(request,'lib/bookpost.html')
def viewbooks(request):
    return render(request,'lib/viewbooks.html')

def add_book(request):
    if request.method == 'POST':
       Book_name = request.POST.get('title')
       Author = request.POST.get('author')
       Publisher = request.POST.get('publisher')
       Publicationdate = request.POST.get('date')
       Genre = request.POST.get('genre')
       Pages=request.POST.get('pages')
       location = request.POST.get('location')
       picture = request.FILES.get('picture')

       book_details = BookDetails(
           Book_name=Book_name,
           Author=Author,
           Publisher=Publisher,
           Publication_date=Publicationdate,
           Genre=Genre,
           Pages=Pages,
           Location=location,
           Picture=picture,
       )
       book_details.save()

       return render(request,'lib/datainserted.html')
    return render(request,'lib/bookpost.html')



def view_books(request):
    book_details_list=BookDetails.objects.all()
    return render(request,'lib/viewbooks.html',{'book_details_list':book_details_list})