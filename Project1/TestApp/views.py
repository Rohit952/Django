from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
from django.http import HttpResponse


def Hello_World(request):
    return HttpResponse('Hello, World!')  # used apps based urls


def home(request):
    return HttpResponse("<h1> This is PYcharm </h1>")  # used project based urls


def date_time_view(request):  # used apps based urls
    date = datetime.now()
    return HttpResponse("The current date and time of the server is : " + str(date))
