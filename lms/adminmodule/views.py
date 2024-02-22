from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def loginpage(request):
    return render(request,'loginpage.html')
def register(request):
    return render(request,'registerpage.html')

def userhomepage(request):
    return render(request,'userhomepage.html')
def libhomepage(request):
    return render(request,'libhomepage.html')