from django.shortcuts import render
from django.http import HttpResponse as httpresponse
def helloWorld(request):
    return httpresponse('HELLO RAJEEV')
# Create your views here.
