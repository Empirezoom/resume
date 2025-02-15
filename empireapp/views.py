from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages 
from .forms import ContactForm


# Create your views here.


def homepage(request):
    cert1= Certification.objects.get(pk=1)
    cert2= Certification.objects.get(pk=2)
    cert3= Certification.objects.get(pk=3)
    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request,'Your message has been sent successfully, I will get back to you shortly!!')
            return redirect('homepage')




    context = {
        'cert1': cert1,
        'cert2': cert2,
        'cert3': cert3,
    }



    return render(request, 'index.html',context)