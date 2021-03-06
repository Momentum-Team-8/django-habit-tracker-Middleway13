from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint

from datetime import date

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
    
class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="habits", null=True)
    name = models.CharField(max_length=256)
    target = models.PositiveIntegerField()
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, null=True, on_delete=models.CASCADE, related_name="records")
    outcome = models.PositiveIntegerField()
    date = models.DateField(default=date.today)
    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_records')
        ]