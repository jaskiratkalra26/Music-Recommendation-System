from django.contrib import admin
from django.urls import path,include
from page import views
import os


urlpatterns = [
    
   path('',views.index,name='index'),
   path('Data', views.Data,name = 'Data')
   
]