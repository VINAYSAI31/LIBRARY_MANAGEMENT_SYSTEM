from django.shortcuts import render

# Create your views here.
def viewbook(request):
    return render(request,'user/viewbook.html')
