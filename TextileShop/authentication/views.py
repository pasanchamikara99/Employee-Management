from http.client import HTTPResponse
from pickle import NONE
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from authentication.models import EmployeesReg
from cryptography.fernet import Fernet
import smtplib


# Create your views here.

def sendMail(fname,email,empID,password):

    subject = "Hello " + fname + "\n Your Employee id is " + empID + "\n User password is  " + password

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    server.login('jayanandanafachion@gmail.com','ncipterepthpugjl')
    server.sendmail('jayanandanafashion@gmail.com',email,subject)


def encryptedPassword(password):
    global key ;
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encpassword = fernet.encrypt(password.encode())
    return encpassword

def decryptedPassword(password):
    #key = Fernet.generate_key()
    fernet = Fernet(key)
    decpassword = fernet.decrypt(password).decode()
    return decpassword




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
                saveRecord = EmployeesReg()
                saveRecord.empid = empID
                saveRecord.fname = fname
                saveRecord.lname = lname
                saveRecord.email = email
                saveRecord.position = position
                saveRecord.password = encryptedPassword(password)
                
                saveRecord.save()

                sendMail(fname,email,empID,password)#call mail function
                messages.success(request,"Employee Registraion sucessfully")

           
           
        
 

    return  render(request,"register.html")




def index(request):
    return  render(request,"index.html")

def login(request):

    if request.method == "POST":
        empID = request.POST['empid']
        password = request.POST.get('password')

        print( "Emp id "+ empID + " password : " + password)



    return  render(request,"user.html")
