from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing), #IP주소/
    path('about_me/', views.about_me), #IP주소/abuot_me/
]
