from django.forms import ModelForm
from django.db import models



class EmployeesReg(models.Model):
    empid = models.CharField(max_length=45)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.EmailField()
    position = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = "Employee"

class EmployeeLeave(models.Model):
    empid = models.CharField(max_length=45)
    date = models.CharField(max_length=45)
    reason = models.CharField(max_length=250)
    class Meta:
        db_table = "employee_leave"

class Leave(models.Model):
    date = models.CharField(max_length=45)
    empid = models.CharField(max_length=45)
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=45)
    class Meta:
        db_table = "leave"


