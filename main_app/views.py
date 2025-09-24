from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def out(request):
    return render(request, 'out.html')

def inside(request):
    return render(request, 'inside.html')


@login_required
def assignments_list(request):
    assignments = Assignment.objects.all()
    return render(request, "assignments_list.html", {"assignments": assignments})

@login_required
def create_assignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = request.user  
            assignment.save()
            return redirect("assignments_list")  
    else:
        form = AssignmentForm()

    return render(request, "assignment_form.html", {"form": form})

