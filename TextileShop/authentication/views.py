from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse

# Create your views here.

def register(request):
    return  render(request,"register.html")
