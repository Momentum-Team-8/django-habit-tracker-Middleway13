from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Habit, HabitRecord 

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_habits")
    
    return render(request, "habits/homepage.html")

@login_required  # this is a decorator or function that will redirect you to login page
def list_habits(request):
    habits = Habit.objects.all()
    return render(request, "habits/list_habits.html", {"habits": habits})