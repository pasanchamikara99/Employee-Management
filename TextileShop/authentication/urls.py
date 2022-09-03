from django.contrib import admin
from django.urls import path,include
from authentication import views

urlpatterns = [
    path('',views.register, name = "register"),
]
