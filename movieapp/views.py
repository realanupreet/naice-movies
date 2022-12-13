from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from movieapp.models import movies
from movieapp.models import movies2, reg
from movieapp.form import regForm
from movieticket import settings
from django.contrib.auth.models import User
from qrcode import *


def index(request):
    m = movies2.objects.all()

    return render(request, 'index.html', {'m': m})


def details(request, id):
    d = movies2.objects.get(id=id)
    print(d.name, request.user, request.user.email)
    subject = f'Ticket booked for {d.name}'

    data = f"""
    Request approved for movie watching for {request.user} with email as {request.user.email} for the movie named {d.name}. Please allow
    """
    img = make(data)
    img.save(settings.MEDIA_ROOT + '/' + "qr.png")
    message = f"""Hi {request.user},
    
    Thanks for your booking for {d.name}.

    Hope you like the movie. Below is the qr code for checking in at the counter.
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]
    email = EmailMessage(
        subject,
        message,
        email_from,
        to=recipient_list,
    )
    email.attach_file('media/qr.png')
    email.send()
    return render(request, 'index.html', {'d': d})
    # send_mail(subject, message, email_from, recipient_list)
