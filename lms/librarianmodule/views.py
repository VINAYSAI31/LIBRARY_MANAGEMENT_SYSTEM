from django.shortcuts import render
from pyexpat.errors import messages

from .models import  *

# Create your views here.
def bookpost(request):
    return render(request,'lib/bookpost.html')
def viewbooks(request):
    return render(request,'lib/viewbooks.html')
def order(request):
    return render(request,'lib/order.html')
def payement(request):
    return render(request,'lib/payement.html')
def card(request):
    return render(request,'lib/card.html')
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


# views.py

from django.shortcuts import render, redirect
from .models import Order  # Import your Order model


def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        adress = request.POST.get('adress')# Assuming the form field name is 'name'
        book = request.POST.get('book')
        quantity = request.POST.get('quantity')

        # Check if required fields are present
        if not name or not book or not quantity:
            return render(request, 'lib/order.html', {'error': 'Missing required fields'})

        # Optional: Validate quantity (e.g., positive integer)
        try:
            quantity = int(quantity)
            if quantity <= 0:
                return render(request, 'lib/order.html', {'error': 'Invalid quantity'})
        except ValueError:
            return render(request, 'lib/order.html', {'error': 'Invalid quantity'})

        # Create order object with customer name
        order = Order.objects.create(name=name, book=book, quantity=quantity, adress=adress)

        # Optionally, you can do additional processing or redirect to a success page
         # Redirect to a success page after order submission

    # If the request method is not POST or if there are validation errors, render the form again
    return render(request, 'lib/order.html')

