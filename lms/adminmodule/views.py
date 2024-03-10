from django.shortcuts import render,redirect
from .forms import FeedbackForm
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def loginpage(request):
    return render(request,'loginpage.html')
def register(request):
    return render(request,'registerpage.html')
def feedback(request):
    return render(request,'feedback.html')
def success(request):
    return render(request,'success.html')


def userhomepage(request):
    return render(request,'userhomepage.html')
def libhomepage(request):
    return render(request,'libhomepage.html')
def locationpage(request):
    return render(request,'location.html')


from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.models import User
from django.contrib import messages


def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        role = request.POST.get('role')  # Get the selected role from the form

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken')
                return render(request, 'registerpage.html')
            else:
                # Create the user with the provided username and password
                user = User.objects.create_user(username=username, password=pass1)

                # Set is_staff based on role
                if role == 'librarian':
                    user.is_staff = True
                else:
                    user.is_staff = False
                user.save()

                messages.info(request, 'Account created successfully!! ')
                return render(request, 'loginpage.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'registerpage.html')
    else:
        return render(request, 'registerpage.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)

            if user.is_staff:  # Check if the user is a staff member (librarian)
                messages.success(request, 'Logged in successfully as librarian!')
                return redirect('libhomepage')
            else:
                messages.success(request, 'Logged in successfully as user!')
                return redirect('userhomepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'loginpage.html')
    else:
        return render(request, 'loginpage.html')


def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Redirect to success page after saving feedback
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

