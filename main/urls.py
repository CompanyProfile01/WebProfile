from django.urls import path
from main.views import show_home, show_services
from django.conf import settings
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('group/<int:number>', show_services, name='show_services'),
]