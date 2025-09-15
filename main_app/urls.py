
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #router.get('/', controller.home)
    path('', views.home, name='home')
]