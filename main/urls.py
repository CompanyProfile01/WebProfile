from django.urls import path
from main.views import show_home
from django.conf import settings
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('', show_home, name='show_home'),

]