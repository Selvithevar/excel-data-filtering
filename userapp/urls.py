from unicodedata import name
from django.urls import path
from . import views as ev



urlpatterns = [
    path('',ev.index,name='index'),

]
