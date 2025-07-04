from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import TourDate, FanMessage
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'TinyBubbles/home.html')

def about(request):
    return render(request, 'TinyBubbles/about.html')

@login_required
def music(request):
    return render(request, 'merchandise.html')

def tour_dates(request):
    dates = TourDate.objects.all().order_by('date')
    return render(request, 'TinyBubbles/tour_dates.html', {'tour_dates': dates})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                message = FanMessage(
                    user=request.user,
                    message=form.cleaned_data['message']
                )
                message.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'TinyBubbles/contact.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'TinyBubbles/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})