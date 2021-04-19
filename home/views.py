from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/contact.html')

def email(request):
    if request.method == 'POST':
        message = request.POST['message']
        sender = request.POST['email_sender']
        subject = f'Website message: {request.POST["subject"]} from {request.POST["email_name"]} ({sender})'
        response = send_mail(subject, message, settings.EMAIL_HOST_USER, ['carlos1014tgn@gmail.com'], 
        fail_silently=False)
        print(response)
    return render(request, 'home/success.html')

def success(request):
    return render(request, 'home/success.html')

def projects(request):
    return render(request, 'home/under_developement.html')

def analytics(request):
    return render(request, 'home/under_developement.html')