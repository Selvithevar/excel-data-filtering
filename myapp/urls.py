from unicodedata import name
from django.urls import path
from . import views as ev



urlpatterns = [
    path('',ev.tablesexcel,name='tablesexcel'),
    path('temp_export/',ev.temp_export,name='temp_export')

]
