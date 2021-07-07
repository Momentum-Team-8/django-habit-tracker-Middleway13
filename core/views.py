from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Habit, HabitRecord 

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_decks")
    return render(request, "core/homepage.html")