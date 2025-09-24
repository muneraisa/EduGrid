from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

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


@login_required
def edit_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

   
    if assignment.teacher != request.user:
        return HttpResponseForbidden("You are not allowed to edit this assignment.")

    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect("assignments_list")
    else:
        form = AssignmentForm(instance=assignment)

    return render(request, "assignment_edit.html", {"form": form})