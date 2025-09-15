from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def out(request):
    return render(request, 'out.html')

def inside(request):
    return render(request, 'inside.html')