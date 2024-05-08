from django.contrib import admin
from django.urls import path,include

from todoapp import views

urlpatterns = [

    path('',views.home,name="home"),
    path('delete/<int:taskid>/', views.delete, name="delete"),
    ]