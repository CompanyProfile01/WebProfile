from django.urls import path
from main.views import show_home, show_services, show_groups, show_portofolio, show_contact, send_email
from django.conf import settings
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('group/<int:number>', show_groups, name='show_groups'),
    path('service/<int:number>', show_services, name='show_services'),
    path('portofolio/', show_portofolio, name='show_portofolio'),
    path('contact/', show_contact, name='show_contact'),
    path('mail/', send_email, name='send_email'),
]