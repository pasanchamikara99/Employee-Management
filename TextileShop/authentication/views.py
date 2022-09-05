from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from authentication.models import EmployeesReg


# Create your views here.

def register(request):


    if request.method == "POST":

        #if request.POST.get('empid') and request.POST['fname'] and request.POST['lname'] and request.POST['email'] and request.POST['position'] and request.POST.get('password') and  request.POST.get('passwordc'): 
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
                saveRecord = EmployeesReg()

                saveRecord.empid = empID
                saveRecord.fname = fname
                saveRecord.lname = lname
                saveRecord.email = email
                saveRecord.password = password

                saveRecord.save()

                messages.success(request,"Employee Registraion sucessfully")

           
           
        
 

    return  render(request,"register.html")

def index(request):


    return  render(request,"index.html")
