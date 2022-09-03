from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.

def register(request):


    if request.method == "POST":
        empID = request.POST['empid']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        position = request.POST['position']
        password = request.POST.get('password')
        passwordc = request.POST.get('passwordc')

        if password != passwordc :
            messages.success(request,"Password mismatch , try again !!! ")
        else:
            print(empID,fname,lname,email,position,password,passwordc)
        


        

    return  render(request,"register.html")

def index(request):


    return  render(request,"index.html")
