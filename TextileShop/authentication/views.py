from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from django.contrib import messages
from authentication.models import EmployeesReg
from cryptography.fernet import Fernet
import smtplib


# Create your views here.

#send employee to his userid and password
def sendMail(fname,email,empID,password):

    subject = "Hello " + fname + "\n Your Employee id is " + empID + "\n User password is  " + password
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('jayanandanafachion@gmail.com','ncipterepthpugjl')
    server.sendmail('jayanandanafashion@gmail.com',email,subject)


#encrypted password
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

                #encp = encryptedPassword(password)
                #decy = decryptedPassword(encp)
                #print(encp)
                #print(decy)

                sendMail(fname,email,empID,password)
                

                messages.success(request,"Employee Registraion sucessfully")

           
           
        
 

    return  render(request,"register.html")

def index(request):


    return  render(request,"index.html")
