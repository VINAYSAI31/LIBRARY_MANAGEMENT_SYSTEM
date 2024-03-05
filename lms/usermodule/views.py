from django.shortcuts import render
from .models import  *



# Create your views here.
def viewbook(request):
    return render(request,'user/viewbook.html')


def view_books(request):
    book_details_list=BookDetails.objects.all()
    return render(request,'user/viewbook.html',{'book_details_list':book_details_list})