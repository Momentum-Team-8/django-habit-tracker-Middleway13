from core.models import Habit
from django.contrib import admin
from .models import User, Habit, HabitRecord, UniqueConstraint

# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(HabitRecord)
admin.site.register(UniqueConstraint)