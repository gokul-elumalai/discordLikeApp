from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World!</h1>")


def room(request):
    return HttpResponse("Room")
