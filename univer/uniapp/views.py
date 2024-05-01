from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def online(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        course = request.POST['course']
        savedata = OnlineForm(firstname=firstname, lastname=lastname, email=email, phone=phone, course=course)
        savedata.save()
        messages.success(request, 'Submitted Successfully!!!')
    return render(request, 'online.html')


def home(request):
    return render(request, 'school.html')


def about(request):
    return render(request, 'about.html')


def course(request):
    return render(request, 'course.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        messagetext = request.POST['message']
        savedata = Contact(name=name, email=email, subject=subject, messagetext=messagetext)
        savedata.save()
        messages.success(request, 'Submitted Successfully!!!')
    return render(request, 'contact.html')