from django.shortcuts import render

# Create your views here.
def bookpost(request):
    return render(request,'lib/bookpost.html')


