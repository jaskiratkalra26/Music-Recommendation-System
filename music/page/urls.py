from django.contrib import admin
from django.urls import path,include
from page import views
import os
os.chdir(r"C:\Users\jaski\OneDrive\Desktop\music_recommendation\music")

urlpatterns = [
    
   path('',views.index,name='index'),
   path('Data', views.Data,name = 'Data')
   
]