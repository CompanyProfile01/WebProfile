from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_home(request):
    return render(request, "index.html")

def show_groups(request, number):
    return render(request, "Groups/group"+ str(number) +".html")

def show_portofolio(request):
    return render(request, "portofolio.html")

def show_contact(request):
    return render(request, "contact.html")

def show_services(request, number):
    if(number == 1):
        return render(request, "Services/auditAdvisory.html")
    elif(number == 2):
        return render(request, "Services/auditServices.html")
    elif(number == 3):
        return render(request, "Services/consulting.html")
    elif(number == 4):
        return render(request, "Services/financialAdvisory.html")
    elif(number == 5):
        return render(request, "Services/humanCapital.html")
    elif(number == 6):
        return render(request, "Services/innovation.html")
    elif(number == 7):
        return render(request, "Services/riskAdvisory.html")
    elif(number == 8):
        return render(request, "Services/taxServices.html")
    elif(number == 9):
        return render(request, "Services/technologyRisk.html")
    