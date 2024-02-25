from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import HttpResponse
from django.core import serializers
from main.models import Visitor, PageViews
from datetime import timedelta, datetime, timezone
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_email(request):
    if request.method == "POST":
        message = request.POST["message"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        send_mail(subject, message, "settings.EMAIL_HOST_USER", [email, "resellcourtesyx@gmail.com"], fail_silently=False)
    return render(request, "contact.html")

def show_home(request):
    ip = get_client_ip(request)
    currentDate = datetime.now(timezone.utc)
    if PageViews.objects.all().count() == 0:
        newPage = PageViews(views = 1)
        newPage.save()
        newVisitor = Visitor(ip = ip, lastVisit = currentDate)
        newVisitor.save()
    else:
        if Visitor.objects.filter(ip = ip).exists():
            visitor = Visitor.objects.filter(ip = ip)
            filteredVisitor = visitor[0]
            lastLogin = filteredVisitor.lastVisit
            dt = currentDate - lastLogin
            hours = dt.seconds / 60 / 60
            if hours>=24:
                pageview = PageViews.objects.all()
                newVisitCount = pageview[0].views + 1
                pageview.update(views = newVisitCount)
            visitor.update(lastVisit = currentDate)
        else:
            newVisitor = Visitor(ip = ip, lastVisit =currentDate)
            newVisitor.save()
            pageview = PageViews.objects.all()
            newVisitCount = pageview[0].views + 1
            pageview.update(views = newVisitCount)
    currentVisitor = PageViews.objects.all()[0].views
    context = {'viewCount' : currentVisitor}
    return render(request, "index.html", context)

def show_groups(request, number):
    return render(request, "Groups/group"+ str(number) +".html")

def show_portofolio(request):
    return render(request, "portofolio.html")

def show_contact(request):
    return render(request, "contact.html")

def show_services(request, number):
    if(number == 1):
        return render(request, "Services/consulting.html")
    elif(number == 2):
        return render(request, "Services/advisory.html")
    elif(number == 3):
        return render(request, "Services/innovation.html")
    elif(number == 4):
        return render(request, "Services/transformation.html")
    elif(number == 5):
        return render(request, "Services/dataAnalytics.html")
    elif(number == 6):
        return render(request, "Services/trainingWorkshop.html")
