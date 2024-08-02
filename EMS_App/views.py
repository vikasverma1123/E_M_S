from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + username)

                subject = 'Welcome to our Event Management Site'
                message = f'Hi {username}, thank you for registering at our site.'
                recipient_list = [email]
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    send_mail('Login Notification', 'You have logged in successfully.', settings.DEFAULT_FROM_EMAIL, [request.user.email])
    return render(request, 'index.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def payment(request):
    return render(request, 'payment.html')

@login_required(login_url='login')
def confirm(request):
    return render(request, 'confirm.html')

def send_event_confirmation_email(event_name, recipient_email, recipient_name, date, time, destination, guest):
    subject = f'Booking Confirmation for {event_name}'
    context = {
        'name': recipient_name,
        'event_name': event_name,
        'date': date,
        'time': time,
        'destination': destination,
        'guest': guest
    }
    message = render_to_string('event_confirmation_email.html', context)
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [recipient_email]
    send_mail(subject, message, email_from, recipient_list, html_message=message)

@login_required(login_url='login')
def technicalevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest = request.POST.get('guest')
        technicalevent = EventAdvisor(name=name, email=email, phone=phone, destination=destination, date=date, time=time, guest=guest, desc=desc)
        technicalevent.save()
        
        # Send confirmation email
        send_event_confirmation_email("Technical Event", email, name, date, time, destination, guest)
        
        return render(request, 'payment.html')
    return render(request, 'technicalevent.html')

@login_required(login_url='login')
def partiesevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest = request.POST.get('guest')
        partiesevent = PartiesEvent(name=name, email=email, phone=phone, destination=destination, date=date, time=time, guest=guest, desc=desc)
        partiesevent.save()
        
        # Send confirmation email
        send_event_confirmation_email("Party Event", email, name, date, time, destination, guest)
        
        return render(request, 'payment.html')
    return render(request, 'partiesevent.html')

@login_required(login_url='login')
def collegeevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest = request.POST.get('guest')
        collegeevent = CollegeEvent(name=name, email=email, phone=phone, destination=destination, date=date, time=time, guest=guest, desc=desc)
        collegeevent.save()
        
        # Send confirmation email
        send_event_confirmation_email("College Event", email, name,date, time, destination, guest)
        
        return render(request, 'payment.html')
    return render(request, 'collegeevent.html')

@login_required(login_url='login')
def eventadvisor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest = request.POST.get('guest')
        eventadvisor = EventAdvisor(name=name, email=email, phone=phone, destination=destination, date=date, time=time, guest=guest, desc=desc)
        eventadvisor.save()
        
        # Send confirmation email
        send_event_confirmation_email("Event Advisor", email, name,date, time, destination, guest)
        
        return render(request, 'payment.html')
    return render(request, 'eventadvisor.html')

@login_required(login_url='login')
def weddingevent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest = request.POST.get('guest')
        weddingevent = WeddingEvent(name=name, email=email, phone=phone, destination=destination, date=date, time=time, guest=guest, desc=desc)
        weddingevent.save()
        
        # Send confirmation email
        send_event_confirmation_email("Wedding Event", email, name,date, time, destination, guest)
        
        return render(request, 'payment.html')
    return render(request, 'weddingevent.html')

@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
