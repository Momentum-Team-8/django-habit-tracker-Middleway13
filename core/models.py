from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    
    def __str__(self):
        return self.username
    
class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    target = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, null=True, on_delete=models.CASCADE, related_name="records")
    outcome = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class UniqueConstraint(fields=['user', 'name', 'date'], name='unique_records')