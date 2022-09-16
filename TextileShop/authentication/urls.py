from django.contrib import admin
from django.urls import path,include
from authentication import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('register',views.register, name = "register"),
    path('login',views.login, name = "login"),
    path('adminpage',views.adminpage, name = "adminpage"),
    path('userpage',views.userpage, name = "userpage"),
    path('changepassword',views.changepassword, name = "changepassword"),
    path('applyleave',views.applyleave, name = "applyleave"),
    path('generatepdf',views.generatepdf, name = "generatepdf"),
    path('update_emp/<id>',views.update_emp, name = "update_emp"),
<<<<<<< HEAD
    path('delete_emp/<id>',views.delete_emp, name = "delete_emp"),
=======
>>>>>>> d3090b1c5bb1c00824d63c614f296f6c042cc954
    path('updateuser',views.updateuser, name = "updateuser"),
]
