#Ive created this

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("This is home page!")