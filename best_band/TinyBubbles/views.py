from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import TourDate, FanMessage
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

def home(request):
    """Home Page for TinyBubbles band

    Args:
        request (_type_): Http request

    Returns:
        _type_: Home.html
    """
    return render(request, 'TinyBubbles/home.html')

def about(request):
    """About Band details

    Args:
        request (_type_): http request

    Returns:
        _type_: About.html
    """
    return render(request, 'TinyBubbles/about.html')

@login_required
def music(request):
    """ Merchandise login 

    Args:
        request (_type_): Http request

    Returns:
        _type_: music.html
    """
    return render(request, 'merchandise.html')

def tour_dates(request):
    """Tour dates page

    Args:
        request (_type_): http request

    Returns:
        _type_: tour dates html
    """
    dates = TourDate.objects.all().order_by('date')
    return render(request, 'TinyBubbles/tour_dates.html', {'tour_dates': dates})

def contact(request):
    """Contact us form

    Args:
        request (_type_): http request
    Returns:
        _type_: Contact.html
    """
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
    """Login page

    Args:
        request (_type_): http request

    Returns:
        _type_: Contact.html
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'TinyBubbles/login.html')

def logout_view(request):
    """Logout page

    Args:
        request (_type_): http request

    Returns:
        _type_: logout.html
    """
    logout(request)
    return redirect('home')

def register_view(request):
    """New user registration

    Args:
        request (_type_): http request

    Returns:
        _type_: logout.html
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})