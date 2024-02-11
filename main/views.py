from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_home(request):
    return render(request, "index.html")

def show_services(request, number):

    return render(request, "Groups/group"+ str(number) +".html")