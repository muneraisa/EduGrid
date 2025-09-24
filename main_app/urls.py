
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #router.get('/', controller.home)
    path('', views.home, name='home'),
    path("assignments/new/", views.create_assignment, name="course_create"),
    path("assignments/", views.assignments_list, name="assignments_list"),
]